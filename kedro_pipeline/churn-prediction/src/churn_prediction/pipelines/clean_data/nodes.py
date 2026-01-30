import pandas as pd
from sklearn.model_selection import train_test_split

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Datumsformat
    df["signup_date"] = pd.to_datetime(df["signup_date"])

    # Zielvariable binär
    df["churn"] = df["churn"].map({"Yes": 1, "No": 0})

    # ungültige Werte entfernen
    df = df.dropna()

    return df

def split_features(df: pd.DataFrame):
    X = df.drop(columns=["churn", "user_id", "signup_date"])
    y = df["churn"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return pd.DataFrame(X_train), pd.DataFrame(X_test), pd.DataFrame(y_train), pd.DataFrame(y_test)