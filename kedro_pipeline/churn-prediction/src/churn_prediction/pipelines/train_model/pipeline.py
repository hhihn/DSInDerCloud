from kedro.pipeline import Pipeline, node
from .nodes import train_model, evaluate_model


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=train_model,
                inputs=["X_train", "y_train"],
                outputs="churn_model",
                name="train_model",
            ),
            node(
                func=evaluate_model,
                inputs=["churn_model", "X_test", "y_test"],
                outputs="model_metrics",
                name="evaluate_model",
            )
        ]
    )