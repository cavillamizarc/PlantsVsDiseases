from argparse import ArgumentParser
from greeneye.database import DatasetBuilder
from greeneye.models.imagenet import ModelBuilder
from greeneye.visualization import VizShower

def make_parser() -> ArgumentParser:
    parser = ArgumentParser(description="CLI to categorize plants diseases among 15 categories")

    parser.add_argument(
            "--image", type=str,
            help="Image to be categorized"
            )
    parser.add_argument(
            "--seed", type=int,
            help="Seed for TF randomization"
            )
    return parser

def main():
    parser = make_parser()
    args = parser.parse_args()
    X = (
            DatasetBuilder(
                dataset_kind = args.ds,
                n_samples = args.n_samples,
                noise = args.noise,
                seed = args.seed
                )
            .build()
            .sample()
            )
    y = (
            ModelBuilder(
                model_type = args.model,
                n_clusters = args.k
                )
            .build()
            .train(X)
            .predict(X)
            )
    VizShower(args.seconds).add_data(X, y).show()
