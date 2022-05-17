import torch
import pandas as pd
from collections import Counter

class Dataset(torch.utils.data.Dataset):

    """
        Constructor
    """
    def __init__(self, args):
        self.args = args
        self.words = self.load_words()
        self.uniq_words = self.get_uniq_words()

        # Mapping between words and indexes
        self.index_to_word = {index: word for index, word in enumerate(self.uniq_words)}
        self.word_to_index = {word: index for index, word in enumerate(self.uniq_words)}

        self.words_indexes = [self.word_to_index[w] for w in self.words]

    """
        Function to load words from the generated dataset
    """
    def load_words(self):
        train_df = pd.read_csv('../created_datasets/str_proc.csv')
        text = train_df['str_notes'].str.cat(sep=' ')
        return text.split(' ')

    """
        Function to get the unique words of our vocabulary
    """
    def get_uniq_words(self):
        word_counts = Counter(self.words)
        return sorted(word_counts, key=word_counts.get, reverse=True)

    def __len__(self):
        return len(self.words_indexes) - self.args.sequence_length

    def __getitem__(self, index):
        return (
            torch.tensor(self.words_indexes[index:index+self.args.sequence_length]),
            torch.tensor(self.words_indexes[index+1:index+self.args.sequence_length+1]),
        )