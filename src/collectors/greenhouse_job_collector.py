"""
Greenhouse Job Collector

Collects jobs from Greenhouse public job boards.
"""


import requests
import pandas as pd
from pathlib import Path
from datetime import datetime



# Test companies using Greenhouse format
# We will expand this list later

GREENHOUSE_BOARDS = {

    "example_company":
    "example"

}



def get_jobs(company_name, board_token):


    url = (
        f"https://boards-api.greenhouse.io/v1/boards/"
        f"{board_token}/jobs"
    )


    try:

        response = requests.get(
            url,
            timeout=20
        )


        if response.status_code != 200:

            return []


        data = response.json()


        jobs = []


        for job in data.get("jobs", []):


            jobs.append({

                "company_name":
                    company_name,


                "job_title":
                    job.get("title"),


                "location":
                    job.get("location", {})
                    .get("name", "Unknown"),


                "job_url":
                    job.get("absolute_url"),


                "source":
                    "Greenhouse",


                "assessment_keywords":
                    "assessment,skills test,coding test",


                "date_collected":
                    datetime.now()
                    .strftime("%Y-%m-%d")

            })


        return jobs


    except Exception as e:

        print(
            f"Error collecting {company_name}: {e}"
        )

        return []




def collect_greenhouse_jobs():


    all_jobs = []


    for company, token in GREENHOUSE_BOARDS.items():

        jobs = get_jobs(
            company,
            token
        )

        all_jobs.extend(jobs)



    df = pd.DataFrame(all_jobs)


    output = Path(
        "data/raw/greenhouse_jobs.csv"
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
        f"Greenhouse jobs created: {output}"
    )




if __name__ == "__main__":

    collect_greenhouse_jobs()