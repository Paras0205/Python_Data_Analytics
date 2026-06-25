# Loop through this list of dicts and print a formatted report using f-strings.
students = [
    {"name": "paras sharma",  "marks": 88, "city": "delhi"},
    {"name": "RAHUL VERMA",   "marks": 45, "city": "MUMBAI"},
    {"name": "priya singh",   "marks": 91, "city": "Pune"},
]

for stu in students:
    name=stu["name"].strip().title()
    marks=stu["marks"]
    city=stu["city"].strip().title()
    status="Status: Passed" if marks>80 else "Status: Failed"
    print(f"Name: {name}, Marks: {marks}, City: {city}, {status}")