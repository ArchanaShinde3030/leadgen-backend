import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leadgen.settings")  # tujhya project name sobat replace kara
django.setup()
# debug_scraper.py

from leads.models import Lead

# Example scraped data (replace with actual scraper output)
scraped_jobs = [
    {
        "company_name": "ABC Tech",
        "job_title": "React Developer",
        "tech_stack": ["React", "Node", "Python"],
        "location": "San Francisco, USA",
        "source_url": "https://example.com/job1",
        "company_website": "https://abc-tech.com",
        "contact_email": "contact@abc-tech.com"
    },
    {
        "company_name": "XYZ Corp",
        "job_title": "Front-end Architect",
        "tech_stack": ["Vue", "Django"],
        "location": "New York, United States",
        "source_url": "https://example.com/job2",
        "company_website": "https://xyz-corp.com",
        "contact_email": "info@xyz-corp.com"
    }
]

for job in scraped_jobs:
    print("=== Scraped Job ===")
    print(f"Company: {job['company_name']}")
    print(f"Title: {job['job_title']}")
    print(f"Location: {job['location']}")
    print(f"Tech Stack: {job['tech_stack']}")
    print(f"URL: {job['source_url']}")

    # Filtering logic (example)
    location_ok = "usa" in job["location"].lower() or "united states" in job["location"].lower()
    title_ok = any(word in job["job_title"].lower() for word in ["developer", "engineer", "software"])
    
    print(f"Location OK: {location_ok}, Title OK: {title_ok}")

    if location_ok and title_ok:
        # Check duplicate
        if not Lead.objects.filter(source_url=job["source_url"]).exists():
            lead = Lead(
                company_name=job["company_name"],
                job_title=job["job_title"],
                tech_stack=", ".join(job["tech_stack"]),
                location=job["location"],
                source_url=job["source_url"],
                company_website=job["company_website"],
                contact_email=job["contact_email"],
                status="new"
            )
            lead.save()
            print("✅ Lead saved!")
        else:
            print("⚠️ Duplicate lead, not saved")
    else:
        print("❌ Lead filtered out due to location/title")
    print("\n")