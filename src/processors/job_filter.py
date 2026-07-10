"""
Job Filter Engine

Filters collected jobs based on:
- Data roles
- Fresher suitability
- Assessment possibility
"""


DATA_ROLE_KEYWORDS = [

    "data analyst",
    "business analyst",
    "analytics analyst",
    "analytics associate",
    "bi analyst",
    "reporting analyst",
    "data scientist",
    "data associate"

]


FRESHER_KEYWORDS = [

    "graduate",
    "entry",
    "junior",
    "associate",
    "intern",
    "trainee",
    "0-2 years",
    "new grad"

]


ASSESSMENT_KEYWORDS = [

    "assessment",
    "test",
    "skills test",
    "coding challenge",
    "case study",
    "technical evaluation"

]



def contains_keyword(text, keywords):

    text = text.lower()

    for keyword in keywords:

        if keyword in text:
            return True

    return False



def classify_job(job):


    title = str(
        job.get("job_title", "")
    )


    description = str(
        job.get("description", "")
    )


    combined_text = (
        title + " " + description
    )


    result = job.copy()


    result["data_role"] = (

        "Yes"
        if contains_keyword(
            combined_text,
            DATA_ROLE_KEYWORDS
        )
        else
        "No"

    )


    result["fresher_suitable"] = (

        "Yes"
        if contains_keyword(
            combined_text,
            FRESHER_KEYWORDS
        )
        else
        "Unknown"

    )


    result["assessment_possible"] = (

        "High"
        if contains_keyword(
            combined_text,
            ASSESSMENT_KEYWORDS
        )
        else
        "Unknown"

    )


    return result