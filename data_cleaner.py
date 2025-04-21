import pandas as pd
import os

def clean_data(input_path="output/raw_data.csv"):
    df = pd.read_csv(input_path)
    df["Price"] = df["Price"].replace("[^0-9.]", "", regex=True).astype(float)
    df["Availability"] = df["Availability"].fillna("Unknown")
    df.to_csv("output/clean_data.csv", index=False)
    return df

if __name__ == "__main__":
    clean_data()