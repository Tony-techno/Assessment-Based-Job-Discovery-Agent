"""
Job Opening Collector

Collects job opportunities from verified companies.
Initial version creates structured job database.
"""

import pandas as pd
from pathlib import Path
from datetime import datetime


def collect_jobs():

    company_file = (
        "data/processed/verified_companies.csv"
    )

    companies = pd.read_csv(company_file)


    jobs = []


    for _, company in companies.iterrows():

        job = {

            "company_name": company["company_name"],

            "job_title": "Data Analyst",

            "job_category": "Data Analytics",

            "experience_level": "Fresher",

            "location": company.get(
                "country",
                "Unknown"
            ),

            "job_url": company.get(
                "career_page",
                "Not Available"
            ),

            "source": "Company Career Page",

            "assessment_keywords": (
                "assessment, analytical test, skills test"
            ),

            "date_collected": datetime.now()
                .strftime("%Y-%m-%d")

        }


        jobs.append(job)


    jobs_df = pd.DataFrame(jobs)


    output = Path(
        "data/raw/jobs_database.csv"
    )


    output.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    jobs_df.to_csv(
        output,
        index=False
    )


    print(
        f"Job database created: {output}"
    )


if __name__ == "__main__":

    collect_jobs()