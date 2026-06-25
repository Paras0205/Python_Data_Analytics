# A scraped job dataset has messy job titles.
# Clean them: strip whitespace, convert to title case, replace short forms,
# and flag if the role is senior (contains "Sr" or "Senior").

titles = [
    "  sr. data analyst  ",
    "DATA SCIENTIST",
    " junior ml engineer",
    "Senior Business Analyst",
    "  data engineer  ",
]
for title in titles:
    cleaned_title = title.strip().title()
    cleaned_title = cleaned_title.replace("Sr.", "Senior")
    is_senior = "Yes" if "Senior" in cleaned_title else "No"
    print(f"Title: {cleaned_title}, Senior Role: {is_senior}")