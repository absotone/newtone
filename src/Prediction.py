import pickle 
from SoundPlayer import * 
from dataset import Dataset
from train import predict
from model import Model
import argparse 

"""
    Load model from file
"""
def get_model(path):
    with open(path, "rb") as f:
        model = pickle.load(f)
        return model

"""
    Get Dataset for Predictions
"""
def get_dataset(args):
    dataset = Dataset(args)
    return dataset


"""
    Prediction Pipeline Class
"""
class Prediction:
    dataset = Dataset
    model = Model
    player = SoundPlayer

    """
        Constructor
    """ 
    def __init__(self, dataset, model, player):
        self.dataset = dataset
        self.model = model 
        self.player = player 

    
    """
        Functions to make and play predictions
    """
    def make_and_play_predictions(self, input_str):

        # Model Predictions
        initial_predictions = predict(self.dataset, self.model, text = input_str)

        # Transforming the predictions
        initial_predictions = " ".join(initial_predictions)

        # Play Sound
        self.player.play(initial_predictions)


if __name__ == "__main__":

    # Getting the arguments 
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-epochs', type=int, default=50)
    parser.add_argument('--batch-size', type=int, default=256)
    parser.add_argument('--sequence-length', type=int, default=10)
    args = parser.parse_args()

    # Dataset
    dataset = get_dataset(args)

    # Model 
    model = get_model("../models/lstm_v2.pkl")

    # Player 
    player = SoundPlayer()

    # Getting predictions
    predictor = Prediction(
        dataset= dataset,
        model = model, 
        player = player
    )

    # Getting the input string from the user 
    print("Enter the input prompt, eg. A5 D6")
    input_str = str(input())

    try:
        predictor.make_and_play_predictions(input_str=input_str)
    except Exception as e:
         print(f"Error in playing your predictions: {e}")
    
    