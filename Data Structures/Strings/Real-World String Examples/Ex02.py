# Parsing — extracting info from text
# Extract domain from email
emails = ["paras@gmail.com", "hr@swiggy.com", "ceo@zomato.in"]

for email in emails:
    parts = email.split("@")
    user   = parts[0]
    domain = parts[1]
    print(f"User: {user}, Domain: {domain}")