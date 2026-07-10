"""
Assessment Company Expander

Creates a curated database of companies
that use assessment-based hiring methods.

Version 1:
50-company seed dataset
"""


import pandas as pd
from pathlib import Path
from datetime import datetime



def create_company_dataset():


    companies = [

        {
            "company_name": "KPMG",
            "industry": "Consulting",
            "country": "India",
            "assessment_platform": "Online Assessment",
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
            "data_roles": "Data Analyst, Business Analyst",
            "fresher_hiring": "Yes"
        },


        {
            "company_name": "Accenture",
            "industry": "IT Services",
            "country": "India",
            "assessment_platform": "Coding Assessment",
            "career_page": "https://www.accenture.com/careers",
            "data_roles": "Data Analyst, AI Analyst",
            "fresher_hiring": "Yes"
        },


        {
            "company_name": "Cognizant",
            "industry": "IT Services",
            "country": "India",
            "assessment_platform": "Skill Assessment",
            "career_page": "https://careers.cognizant.com",
            "data_roles": "Analyst, Data Analyst",
            "fresher_hiring": "Yes"
        },


        {
            "company_name": "TCS",
            "industry": "IT Services",
            "country": "India",
            "assessment_platform": "TCS iON Assessment",
            "career_page": "https://www.tcs.com/careers",
            "data_roles": "Data Analyst, BI Analyst",
            "fresher_hiring": "Yes"
        },


        {
            "company_name": "Infosys",
            "industry": "IT Services",
            "country": "India",
            "assessment_platform": "Online Assessment",
            "career_page": "https://www.infosys.com/careers",
            "data_roles": "Data Analyst, Data Associate",
            "fresher_hiring": "Yes"
        },


        {
            "company_name": "Wipro",
            "industry": "IT Services",
            "country": "India",
            "assessment_platform": "Online Test",
            "career_page": "https://careers.wipro.com",
            "data_roles": "Analyst, Data Engineer",
            "fresher_hiring": "Yes"
        },


        {
            "company_name": "EY",
            "industry": "Consulting",
            "country": "India",
            "assessment_platform": "Online Assessment",
            "career_page": "https://ey.com/careers",
            "data_roles": "Data Analyst, Consultant",
            "fresher_hiring": "Yes"
        },


        {
            "company_name": "PwC",
            "industry": "Consulting",
            "country": "India",
            "assessment_platform": "Assessment Test",
            "career_page": "https://pwc.com/careers",
            "data_roles": "Data Analyst, Analytics Associate",
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


    # Add tracking fields

    df["source"] = "Curated Assessment Hiring Database"

    df["evidence"] = ""

    df["confidence"] = "Medium"

    df["collected_date"] = (
        datetime.now()
        .strftime("%Y-%m-%d")
    )


    df["priority_score"] = 50



    output = Path(
        "data/raw/assessment_companies.csv"
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
        f"Assessment company database created: {output}"
    )



if __name__ == "__main__":

    create_company_dataset()