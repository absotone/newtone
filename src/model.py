import torch
from torch import nn

class Model(nn.Module):

    """
        Constructor
    """
    def __init__(self, dataset):
        super(Model, self).__init__()

        # LSTM Parameters
        self.lstm_size = 128
        self.embedding_dim = 128
        self.num_layers = 5

        n_vocab = len(dataset.uniq_words)
        
        # Embedding Layer
        self.embedding = nn.Embedding(
            num_embeddings=n_vocab,
            embedding_dim=self.embedding_dim,
        )

        # LSTM Layer
        self.lstm = nn.LSTM(
            input_size=self.lstm_size,
            hidden_size=self.lstm_size,
            num_layers=self.num_layers,
            dropout=0.5,
        )

        # Fully Connected Layer
        self.fc = nn.Linear(self.lstm_size, n_vocab)

    """
        Forward propagation:
            - Embedding
            - LSTM
            - Fully Connected
    """
    def forward(self, x, prev_state):
        embed = self.embedding(x)
        output, state = self.lstm(embed, prev_state)
        logits = self.fc(output)
        return logits, state

    """
        Helper function to return tensors corresponding to the initial state of the network
    """
    def init_state(self, sequence_length):
        return (torch.zeros(self.num_layers, sequence_length, self.lstm_size),
                torch.zeros(self.num_layers, sequence_length, self.lstm_size))