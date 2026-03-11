
import spacy
import re

nlp = spacy.load("en_core_web_sm")

# Developer roles
VALID_ROLES = [
    "developer",
    "engineer",
    "software engineer",
    "frontend",
    "backend",
    "back-end",
    "full stack",
    "full-stack",
    "data engineer",
    "ai engineer",
    "platform engineer",
]

# Tech stack keywords
TECH_KEYWORDS = ["react","node","python","django","vue","angular","aws","java"]

# USA keywords & cities
USA_KEYWORDS = [
    "usa",
    "united states",
    "us",
    "u.s",
    "u.s.",
    "remote us",
    "us remote",
    "remote usa",
    "remote united states",
    "united states only",
    "anywhere in us"
]

USA_CITIES = [
    "new york","san francisco","los angeles","chicago","austin","seattle",
    "boston","miami","denver","atlanta","houston","philadelphia",
    "dallas","san diego","san jose","detroit","north carolina","georgia",
    "texas","florida","virginia"
]

def clean_location(location):
    """Remove emojis and symbols"""
    location = re.sub(r'[^\w\s,]', '', location)
    return location.lower().strip()

def location_match(location):
    if not location:
        print("Rejected location: empty")
        return False

    loc = clean_location(location)
    print(f"Checking location: {loc}")

    # Reject remote jobs
    if "remote" in loc:
        print("Rejected location: remote job")
        return False

    # ✅ Allow only USA cities
    if any(city in loc for city in USA_CITIES):
        return True

    print("Rejected location: not a target USA city")
    return False

def role_match(job_title):
    job_title = job_title.lower()
    return any(role in job_title for role in VALID_ROLES)

def is_valid_lead(job_title, location, description):
    # 1. Location check
    if not location_match(location):
        print("Rejected location:", location)
        return False

    # 2. Role check
    if not role_match(job_title):
        print("Rejected role:", job_title)
        return False

    # 3. Tech check (optional)
    techs = extract_tech_stack(description)

    if techs:
        print(f"VALID: {job_title} | Tech: {techs}")
    else:
        print(f"VALID: {job_title} | Tech: Not specified")

    return True

def extract_tech_stack(description):
    text = description.lower()
    found = [tech for tech in TECH_KEYWORDS if tech in text]
    return ", ".join(found)

