import pandas as pd
from sklearn.preprocessing import StandardScaler

def engineer_features(df):
    print("🛠️  Applying feature engineering...")

    df["Amount_x_Returns"] = df["Total Purchase Amount"] * df["Returns"]
    df["Age_Squared"] = df["Age"] ** 2
    df["Price_per_Unit"] = df["Total Purchase Amount"] / (df["Quantity"] + 1)

    print("✅ Feature engineering completed.")
    return df

