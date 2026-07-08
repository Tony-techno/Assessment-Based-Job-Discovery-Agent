"""
Company Source Collector

Creates initial company database
for assessment based hiring research.
"""

import pandas as pd
from pathlib import Path


def collect_companies():

    companies = [

        {
            "company_name": "KPMG",
            "industry": "Consulting",
            "country": "India",
            "assessment_platform": "Possible TestGorilla/Assessment",
            "career_page": "https://kpmg.com/careers",
            "data_roles": "Data Analyst, Analyst",
            "fresher_hiring": "Yes"
        },

        {
            "company_name": "Deloitte",
            "industry": "Consulting",
            "country": "India",
            "assessment_platform": "Online Assessment",
            "career_page": "https://www.deloitte.com/careers",
            "data_roles": "Analyst, Data Analyst",
            "fresher_hiring": "Yes"
        },

        {
            "company_name": "Revolut",
            "industry": "FinTech",
            "country": "Global",
            "assessment_platform": "Skill Assessment",
            "career_page": "https://www.revolut.com/careers",
            "data_roles": "Data Analyst",
            "fresher_hiring": "Yes"
        }

    ]


    df = pd.DataFrame(companies)


    output_path = Path(
        "data/raw/company_database.csv"
    )


    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    df.to_csv(
        output_path,
        index=False
    )


    print(
        f"Company database created: {output_path}"
    )


if __name__ == "__main__":
    collect_companies()