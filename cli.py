#!/bin/python

from argparse import ArgumentParser
#from greeneye.database import DatasetBuilder
#from greeneye.models.imagenet import ModelBuilder
#from greeneye.preprocessing.imagenetPrepros import Preprocessor
import joblib

parser: ArgumentParser

def make_parser() -> ArgumentParser:
   
    parser = ArgumentParser(description="CLI to categorize plants diseases among 38 categories")

    subparsers = parser.add_subparsers(help="Sub-commands help")

    parser_train = subparsers.add_parser("train", help="Train a model")
    parser_train.add_argument(
        "--model","-m",
        required=False, # False for the moment. Only one model available
        help="name of the deep learning architecture to use",
    )
    parser_train.add_argument(
        "--path", "-p",
        required=True,
        help="Path to the directory where to save the model",
    )
    parser_train.set_defaults(func=train)

    parser_pred = subparsers.add_parser("predict", help="Use a model for prediction")
    parser_pred.add_argument(
        "--model_path", "-mp",
        required=True,
        help="Path to the model to use for prediction"
    )
    parser_pred.add_argument(
        "--sample_path", "-sp",
        required=True,
        help="Path to the sample to be predicted"
    )
    parser_pred.set_defaults(func=predict)

    args = parser.parse_args()
    args.func(args)

    return parser

def train(args):
    print("Training model with:")
    for k, v in args.__dict__.items():
        print(f"{k}={v}")




def predict(args):
    print("Predicting with:")
    for k, v in args.__dict__.items():
        print(f"{k}={v}")

    model = joblib.load(args.model_path)
    model.summary()
    #X = Preprocessor().img




def main():
    parser = make_parser()
    args = parser.parse_args()
    #print("Starting")
    """ if(args.image == "test"):

        print("This is just a test")
 
        #

   
        #
        #result = model.predict(X)
        
        #print(result)
    else:
        print("noi") """


main()