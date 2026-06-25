#Resume keyword scanner

resume = """
Experienced in Python, SQL, Power BI, and Excel.
Built machine learning models using Scikit-learn.
Created dashboards for business stakeholders.
"""

keywords = ["python","sql","tableau","power bi","excel",
            "machine learning","spark","data cleaning","scikit-learn"]

resume_lower = resume.lower()
found = []
missing = []

for kw in keywords:
    if kw in resume_lower:
        found.append(kw)
    else:
        missing.append(kw)

score = len(found) / len(keywords) * 100

print(f"✓ Found   : {', '.join(found)}")
print(f"✗ Missing : {', '.join(missing)}")
print(f"\nMatch score: {score:.1f}%")