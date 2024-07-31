# Import necessary libraries
from transformers import BertModel, BertTokenizer
import torch
from torch import nn

# Random seed for reproducibilty
RANDOM_SEED = 42
torch.manual_seed(RANDOM_SEED)
torch.cuda.empty_cache()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")



# Set the model name
model_name = 'prajjwal1/bert-tiny'

# Build a BERT based tokenizer
tokenizer = BertTokenizer.from_pretrained(model_name, force_download=True)


max_tweets = 60
max_len = 100
batch_size = 1 # this is because its used for so much, and really the input will only be one example so it just makes things easier

num_lstms = 6

# Build the Sentiment Classifier class
class SentimentClassifier(nn.Module):

    # Constructor class
    def __init__(self, n_classes):
        super(SentimentClassifier, self).__init__()
        self.bert = BertModel.from_pretrained(model_name) #Bert model
        self.drop = nn.Dropout(p=0.3) # dropout layer

        self.lstm = nn.ModuleList([nn.LSTM(input_size=128, hidden_size=50, num_layers=6, batch_first=True).to(device) for _ in range(num_lstms)]) #list of LSTMS we use to process the output from each BERT
        self.batch = torch.nn.BatchNorm1d(self.lstm[0].hidden_size * num_lstms) #Batch normalization layer
        self.out = nn.Sequential(nn.Linear(self.lstm[0].hidden_size*num_lstms, 1), nn.Sigmoid()) # linear layer to map outputs to score
        

    # Forward propagation class
    def forward(self, input_ids, attention_mask):
        pooled_output = torch.zeros((batch_size, max_tweets, 128), dtype=torch.float32).to(device) # output of BERT models has to be this size, for each batch there is a vector of 128 for each tweet

        for x in range(0 , len(input_ids)): # loop through all the tweets
            _, output = self.bert(input_ids=input_ids[x], attention_mask=attention_mask[x], return_dict=False) # output from the BERT model
            output = output.to(device)
            pooled_output[:, x].copy_(output) # set its value in the array
        
        pooled_output = pooled_output.view(batch_size, num_lstms, max_tweets//num_lstms, 128) #resize in order to input into each LSTM

        lstmOut = torch.zeros((batch_size, num_lstms, self.lstm[0].hidden_size), dtype=torch.float32).to(device) #ouotput of the LSTMS will be 50 for each LSTM in a batch
        
        for i in range(len(self.lstm)): # go through each LSTM
            lstmTempOut, _ = self.lstm[i](pooled_output[:, i, :]) # get the output of the LSTM on its dataset
            lstmOut[:, i, :] = lstmTempOut[:, -1, :]# little reshaping in order to make things easy for the linear layer
        lstmOut = self.drop(lstmOut)
        lstmOut = lstmOut.view(batch_size, num_lstms*self.lstm[0].hidden_size)# flatten
        norm = self.batch(lstmOut)# batch normalizing
        
       
        return self.out(norm)# return the output from the linear layer
    

model = SentimentClassifier(len(['not depressed', 'depressed']))
model.load_state_dict(torch.load("multi_post_model.pt", map_location=torch.device('cuda')))
model = model.to(device)


def encodeArray(strArr):
    encoding = [
            tokenizer.encode_plus(
                x,
                add_special_tokens=True,
                max_length=max_len,
                return_token_type_ids=False,
                padding = 'max_length',
                truncation = True,
                return_tensors='pt',
            ) for x in strArr
        ]

    return {
        'review_text': strArr,
        'input_ids': [x['input_ids'].flatten() for x in encoding],
        'attention_mask': [x['attention_mask'].flatten() for x in encoding],

    }
#print(encodeArray(["hi", "Hey look buddy, I'm a Warhammer player. That means I solve problems, not problems like"]))

def returnScore(input):
    while len(input) < max_tweets:
        input.append("")
    
    d = encodeArray(input)
    
    input_ids = torch.stack(d["input_ids"])[None, :, :]
    attention_mask = torch.stack(d["attention_mask"])[None, :, :]
    
    input = torch.zeros((max_tweets, batch_size, max_len)).to(device)
    for x in range(max_tweets):
        input[x].copy_(input_ids[:, x])

    attention = torch.zeros((max_tweets, batch_size, max_len)).to(device)
    for x in range(max_tweets):
        attention[x].copy_(attention_mask[:, x])
        
    model.eval()
    return model.forward(input.to(torch.int64), attention.to(torch.int64)).item()

