#!/bin/python

from argparse import ArgumentParser
#from greeneye.database import DatasetBuilder
from greeneye.models.models import Imagenet
from greeneye.preprocessing.Pre import ImagenetPre
import joblib
import tensorflow as tf
import numpy as np

parser: ArgumentParser

def make_parser() -> ArgumentParser:
   
    parser = ArgumentParser(description="CLI to categorize plants diseases among 38 categories")

    subparsers = parser.add_subparsers(help="Sub-commands help")

    parser_train = subparsers.add_parser("train", help="Train a model")
    parser_train.add_argument(
        "--model","-m",
        required=False, # False for the moment. Only one model available
        help="name of the deep learning architecture to use",
        choices=list("imagenet_FT")
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

    ## Missing support for more datasets
    #ds = DatasetBuilder().build()
    #X = ds.getData()

    ## Aquí pondría condiciones para usar otros modelos...
    ## Si tuviera otros modelos :')
    #model = ModelBuilder.build(args.model).train(X)
    #model.save(args.path)

## ie: python cli.py predict --mp "./greeneyeModel.joblib" -sp "./greeneye/database/DB/test/test/CornCommonRust1.JPG"
def predict(args):
    print("--Predicting with:")
    for k, v in args.__dict__.items():
        print(f"{k}={v}")

    print(args.model_path)

    ## Loading of the model
    model = joblib.load(args.model_path, mmap_mode='r')
    model.summary()

    ## Image preprocessing
    X = ImagenetPre.imgPreprocess(args.sample_path)

    ## Prediction and decoding
    #for a in model.predict(ims_prep):
    #    i = a.argmax()
    #    print(class_dict[i])


def main():
    parser = make_parser()
    args = parser.parse_args()

main()