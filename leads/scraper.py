
import requests
USA_KEYWORDS = [
    "usa",
    "united states",
    "us",
    "remote us",
    "remote usa"
]
def is_usa_based(location, description):
    text = f"{location} {description}".lower()

    for keyword in USA_KEYWORDS:
        if keyword in text:
            return True

    return False

TECH_KEYWORDS = [
    "developer", "engineer", "python", "java",
    "react", "node", "backend", "frontend",
    "fullstack", "software"
]
def is_valid_lead(job_title, tech_stack):
    text = f"{job_title} {tech_stack}".lower()

    for keyword in TECH_KEYWORDS:
        if keyword in text:
            return True

    return False

def fetch_jobs():
    url = "https://remoteok.com/api"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    data = response.json()

    jobs = []

    for job in data[1:]:  # skip metadata

        title = job.get("position", "")
        company = job.get("company", "")

        # ✅ FIX: multiple location sources
        location = (
            job.get("candidate_required_location")
            or job.get("location")
            or job.get("region")
            or ""
        )

        tags = job.get("tags", [])
        source_url = job.get("url", "")
        description = job.get("description", "")

        jobs.append({
            "job_title": title,
            "company_name": company,
            "location": location,
            "source_url": source_url,
            "tech_stack": ", ".join(tags),
            "description": description,
            
        })

    return jobs