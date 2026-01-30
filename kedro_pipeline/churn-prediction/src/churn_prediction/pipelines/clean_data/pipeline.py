from kedro.pipeline import Pipeline, node
from .nodes import clean_data, split_features


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=clean_data,
                inputs="users_raw",
                outputs="users_clean",
                name="clean_data",
            ),
            node(
                func=split_features,
                inputs="users_clean",
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split_data",
            )
        ]
    )