import os
import django

# ✅ Django setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leadgen.settings")
django.setup()

import re
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright, TimeoutError
from leads.models import Lead


# -------------------
# Keywords / Config
# -------------------
VALID_ROLES = [
    "developer", "software engineer", "frontend", "back-end", "backend",
    "full stack", "full-stack", "data engineer", "ai engineer", "architect",
    "programmer"
]

TECH_KEYWORDS = ["react","node","python","django","vue","angular","aws","java"]

USA_KEYWORDS = ["usa","united states","us","remote united states"]

USA_CITIES = [
    "new york","san francisco","los angeles","chicago","austin","seattle",
    "boston","miami","denver","atlanta","houston","philadelphia",
    "dallas","san diego","san jose","detroit","north carolina","georgia",
    "texas","florida","virginia"
]

# -------------------
# Helper Functions
# -------------------
def clean_text(text):
    text = re.sub(r'[^\w\s,]', '', text)
    return text.lower().strip()

def location_match(location):
    loc = clean_text(location)
    return any(city in loc for city in USA_CITIES) or any(k in loc for k in USA_KEYWORDS)

def role_match(title):
    title = title.lower()
    return any(role in title for role in VALID_ROLES)

def extract_tech_stack(description):
    text = description.lower()
    found = [tech for tech in TECH_KEYWORDS if tech in text]
    return ", ".join(found)

def is_valid_lead(title, location, description=""):
    if not location_match(location):
        print(f"DEBUG: rejected due to location -> {location}")
        return False
    if not role_match(title):
        print(f"DEBUG: rejected due to role -> {title}")
        return False
    return True

# -------------------
# Scraper Functions
# -------------------
def scrape_jobs(url, site_type="greenhouse"):
    jobs = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto(url, timeout=60000)
            page.wait_for_load_state("load", timeout=60000)
        except TimeoutError:
            print(f"⚠️ Timeout loading {url}")
            browser.close()
            return jobs

        html = page.content()
        soup = BeautifulSoup(html, "html.parser")

        if site_type == "greenhouse":
            job_cards = soup.select("div.opening")
            for card in job_cards:
                a_tag = card.find("a")
                if not a_tag:
                    continue
                title = a_tag.text.strip()
                job_url = "https://boards.greenhouse.io" + a_tag['href']
                location = card.find("span", class_="location").text.strip() if card.find("span", class_="location") else ""
                jobs.append({
                    "company_name": url.split("//")[1].split("/")[0],
                    "job_title": title,
                    "location": location,
                    "description": title,
                    "source_url": job_url,
                    "company_website": f"https://{url.split('//')[1].split('/')[0]}",
                    "contact_email": ""
                })

        elif site_type == "lever":
            job_cards = soup.select("div.posting")
            for card in job_cards:
                a_tag = card.find("a")
                if not a_tag:
                    continue
                title = a_tag.text.strip()
                location_tag = card.find("span", class_="sort-by-location")
                location = location_tag.text.strip() if location_tag else "Remote, United States"
                jobs.append({
                    "company_name": url.split("//")[1].split("/")[0],
                    "job_title": title,
                    "location": location,
                    "description": title,
                    "source_url": a_tag['href'],
                    "company_website": f"https://{url.split('//')[1].split('/')[0]}",
                    "contact_email": ""
                })

        elif site_type == "remotive":
            job_cards = soup.select("div.job-tile")
            for card in job_cards:
                title_tag = card.select_one("h2 a")
                if not title_tag:
                    continue
                title = title_tag.text.strip()
                location_tag = card.select_one("span.location")
                location = location_tag.text.strip() if location_tag else ""
                jobs.append({
                    "company_name": "Remotive",
                    "job_title": title,
                    "location": location,
                    "description": title,
                    "source_url": "https://remotive.io" + title_tag['href'],
                    "company_website": "https://remotive.io",
                    "contact_email": ""
                })

        browser.close()
    return jobs

# -------------------
# Main Scraper Run
# -------------------
def run_scraper_main():
    urls = [
        ("https://boards.greenhouse.io/stripe", "greenhouse"),
        ("https://jobs.lever.co/notion", "lever"),
        ("https://remotive.io/remote-jobs/software-dev", "remotive")
    ]

    saved_count = 0
    rejected_count = 0

    for url, site_type in urls:
        jobs = scrape_jobs(url, site_type)
        for job in jobs:
            if is_valid_lead(job["job_title"], job["location"], job["description"]):
                if not Lead.objects.filter(source_url=job["source_url"]).exists():
                    lead = Lead(
                        company_name=job["company_name"],
                        job_title=job["job_title"],
                        tech_stack=extract_tech_stack(job["description"]),
                        location=job["location"],
                        source_url=job["source_url"],
                        company_website=job["company_website"],
                        contact_email=job["contact_email"],
                        status="new"
                    )
                    lead.save()
                    saved_count += 1
                    print(f"SAVED -> {job['job_title']} | {job['location']}")
                else:
                    print(f"DUPLICATE -> {job['job_title']} | {job['location']}")
            else:
                rejected_count += 1

    print(f"Scraping finished | Saved: {saved_count} | Rejected: {rejected_count}")

# -------------------
# Run directly
# -------------------
if __name__ == "__main__":
    run_scraper_main()