"""
Company Data Cleaner

Combines discovered company data
and creates verified database.
"""

import pandas as pd
from pathlib import Path


def clean_companies():

    files = [
        "data/raw/company_database.csv",
        "data/raw/discovered_companies.csv"
    ]


    dataframes = []


    for file in files:

        df = pd.read_csv(file)

        dataframes.append(df)


    combined = pd.concat(
        dataframes,
        ignore_index=True,
        sort=False
    )


    # Normalize company names

    combined["company_name"] = (
        combined["company_name"]
        .str.strip()
        .str.title()
    )


    # Remove duplicates

    combined = combined.drop_duplicates(
        subset=["company_name"]
    )


    # Add priority score

    combined["priority_score"] = 0


    combined.loc[
        combined["fresher_hiring"]=="Yes",
        "priority_score"
    ] += 50


    combined.loc[
        combined["confidence"]=="High",
        "priority_score"
    ] += 50


    output = Path(
        "data/processed/verified_companies.csv"
    )


    output.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    combined.to_csv(
        output,
        index=False
    )


    print(
        f"Verified database created: {output}"
    )


if __name__ == "__main__":
    clean_companies()