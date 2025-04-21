import pandas as pd
import os

def generate_reports(input_path="output/clean_data.csv"):
    df = pd.read_csv(input_path)
    df.to_csv("output/report.csv", index=False)

    html = df.to_html(index=False)
    with open("output/report.html", "w") as f:
        f.write(html)
    return df

if __name__ == "__main__":
    generate_reports()