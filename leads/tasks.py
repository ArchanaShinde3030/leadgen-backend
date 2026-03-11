
import re
import requests
import spacy
from celery import shared_task
from leads.ai_filter import is_valid_lead
from leads.scraper import fetch_jobs
from leads.models import Lead
nlp = spacy.load("en_core_web_sm")

US_KEYWORDS = ["usa", "united states", "u s", "us"]

def is_usa_based(location):
    if not location or location.strip() == "":
        print("Rejected location: empty")
        return False

    loc = location.lower().replace(".", "").strip()

    if any(word in loc for word in US_KEYWORDS):
        return True

    if "," in loc and "usa" in loc:
        return True

    print(f"Rejected location: {location}")
    return False
@shared_task
def run_scraper():
    jobs = fetch_jobs()
    saved_count = 0
    for job in jobs:
        if is_valid_lead(job.get("job_title"), job.get("location"), job.get("description")):
            Lead.objects.get_or_create(
                job_title=job.get("job_title"),
                company_name=job.get("company_name"),
                location=job.get("location"),
                source_url=job.get("source_url"),
                tech_stack=job.get("tech_stack"),
                description=job.get("description"),
            )
            saved_count += 1
    print(f"✅ Leads saved: {saved_count}")
    return saved_count
