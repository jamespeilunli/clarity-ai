# Import necessary libraries
from transformers import BertModel, BertTokenizer
import torch
from torch import nn

# Random seed for reproducibilty
RANDOM_SEED = 42
torch.manual_seed(RANDOM_SEED)

# Set GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class_names = ['not depressed', 'depressed']

# Set the model name
MODEL_NAME = 'prajjwal1/bert-tiny'

# Build a BERT based tokenizer
tokenizer = BertTokenizer.from_pretrained(MODEL_NAME, force_download=True)
MAX_LEN = 160
bert_model = BertModel.from_pretrained(MODEL_NAME)
# Build the Sentiment Classifier class
class SentimentClassifier(nn.Module):

    # Constructor class
    def __init__(self, n_classes):
        super(SentimentClassifier, self).__init__()
        self.bert = BertModel.from_pretrained(MODEL_NAME)
        self.drop = nn.Dropout(p=0.3)
        self.out = nn.Linear(self.bert.config.hidden_size, 1)

    # Forward propagaion class
    def forward(self, input_ids, attention_mask):
        _, pooled_output = self.bert(
          input_ids=input_ids,
          attention_mask=attention_mask,
          return_dict=False
        )
        #  Add a dropout layer
        output = self.drop(pooled_output)
        return torch.sigmoid(self.out(output))

test = torch.load("single_post_model.pt", map_location=torch.device('cuda'))
model = SentimentClassifier(len(class_names))
model.load_state_dict(test)
model = model.to(device)

def returnScore(input):
    encoded_review = tokenizer.encode_plus(
        input,
        max_length=MAX_LEN,
        add_special_tokens=True,
        return_token_type_ids=False,
        pad_to_max_length=True,
        return_attention_mask=True,
        return_tensors='pt',
    )
    input_ids = encoded_review['input_ids'].to(device)
    attention_mask = encoded_review['attention_mask'].to(device)

    output = model(input_ids, attention_mask)
    _, prediction = torch.max(output, dim=1)

    print(input)
    print(f'Sentiment  : {output[0][0]}')

    return float(output[0][0])
