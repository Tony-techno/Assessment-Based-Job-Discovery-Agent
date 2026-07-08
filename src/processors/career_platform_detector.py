"""
Career Platform Detector

Detects job hosting platforms
from company career URLs.
"""

import pandas as pd
from pathlib import Path


def detect_platform(url):

    if pd.isna(url):
        return "Unknown"


    url = str(url).lower()


    if "greenhouse" in url:
        return "Greenhouse"


    elif "lever" in url:
        return "Lever"


    elif "workday" in url:
        return "Workday"


    elif "smartrecruiters" in url:
        return "SmartRecruiters"


    else:
        return "Custom Career Page"



def process_companies():

    input_file = (
        "data/processed/verified_companies.csv"
    )


    df = pd.read_csv(input_file)


    df["career_platform"] = (
        df["career_page"]
        .apply(detect_platform)
    )


    output = Path(
        "data/processed/companies_with_platform.csv"
    )


    output.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    df.to_csv(
        output,
        index=False
    )


    print(
        f"Platform detection completed: {output}"
    )



if __name__ == "__main__":
    process_companies()