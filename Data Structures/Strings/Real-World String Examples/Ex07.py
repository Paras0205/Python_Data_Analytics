# Given a list of raw job strings, extract company name and role separately.
jobs = [
    "Swiggy | Data Analyst | Delhi",
    "Zomato | Data Scientist | Bengaluru",
    "Paytm  | Business Analyst | Noida",
]

for job in jobs:
    parts=job.split("|")
    company=parts[0].strip()
    role=parts[1].strip()
    print(f"Company: {company}, Role: {role}")