from kedro.pipeline import Pipeline, node
from .nodes import train_model, evaluate_model


def create_pipeline(**kwargs):
    return Pipeline(
        [

        ]
    )