
from openai_tools import get_job_listings

def search_jobs(skills, preferences):
    prompt = f"Find jobs related to AI that match the following skills: {skills} and preferences: {preferences}."
    job_listings = get_job_listings(prompt)
    return job_listings
