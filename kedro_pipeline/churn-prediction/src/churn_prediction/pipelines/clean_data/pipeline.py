from kedro.pipeline import Pipeline, node
from .nodes import clean_data, split_features


def create_pipeline(**kwargs):
    # eine pipeline ist eine reihe an nodes die ausgeführt werden sollen
    # jedem node gebe ich einen input, einen output sowie einen namen
    return Pipeline(
        [
            # der 1. node
            # säubert die daten und speichert sie ab
            node(func=clean_data,
                 inputs="users_raw",
                 outputs="users_clean",
                 name="clean_data"),
            # der 2. node
            # teilt die gereinigten daten in einen test/train split auf und
            # speichert diesen ab
            node(func=split_features,
                 inputs="users_clean",
                 outputs=["X_train", "X_test", "y_train", "y_test"],
                 name="split_data")
        ]
    )