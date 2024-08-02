from torch.utils.data import Dataset, DataLoader
import torch
class TweetDataset(Dataset):
    # Constructor Function
    def __init__(self, reviews, targets, tokenizer, max_len):
        self.reviews = reviews
        self.targets = targets
        self.tokenizer = tokenizer
        self.max_len = max_len

    # Length magic method
    def __len__(self):
        return len(self.reviews)

    # get item magic method
    def __getitem__(self, item):
        review = self.reviews[item]
        target = self.targets[item]

        # Encoded format to be returned
        encoding = [
            self.tokenizer.encode_plus(
                x,
                add_special_tokens=True,
                max_length=self.max_len,
                return_token_type_ids=False,
                padding = 'max_length',
                truncation = True,
                return_tensors='pt',
            ) for x in review
        ]

        return {
            'review_text': review,
            'input_ids': [x['input_ids'].flatten() for x in encoding],
            'attention_mask': [x['attention_mask'].flatten() for x in encoding],
            'targets': torch.tensor(target, dtype=torch.long)
        }