# Case methods

s = "paras SHARMA from delhi"

print(s.upper())                 # PARAS SHARMA FROM DELHI
print(s.lower())                 # paras sharma from delhi
print(s.title())                 # Paras Sharma From Delhi
print(s.capitalize())            # Paras sharma from delhi
print(s.swapcase())              # PARAS sharma FROM DELHI
print(s.replace("from","FROM"))  # paras SHARMA FROM delhi

# Use .title() to clean messy name data. Use .lower() before comparing strings so "Delhi" == "delhi" works.

# Search & check methods

s = "  Hello, I am Paras  "

# Find position
print(s.find("Paras"))      # 14 (index where it starts)
print(s.find("xyz"))        # -1 (not found, no error)
print(s.count("a"))         # 2

# Check start/end
email = "paras@gmail.com"
print(email.startswith("paras"))   # True
print(email.endswith(".com"))      # True

# Check content type
print("Paras".isalpha())    # True — only letters (Returns True if all characters in the string are alphabetic (a-z or A-Z).)
print("123".isnumeric())    # True — only numbers
print("  ".isspace())       # True — only spaces
print("123".isdigit())       # True — only digits  (Returns True if all characters are digits (0-9 only)).
print("Paras123".isalnum())  # True — letters + numbers

# Clean & modify methods

s = "  Hello World  "

# Remove whitespace
print(s.strip())            # "Hello World"
print(s.lstrip())           # "Hello World  "
print(s.rstrip())           # "  Hello World"

# Replace
print(s.replace("World","Paras"))  # "  Hello Paras  "

# Split — converts string to list
sentence = "Delhi Mumbai Pune Kolkata"
cities = sentence.split(" ")
print(cities)       # ['Delhi','Mumbai','Pune','Kolkata']

# Join — converts list back to string
joined = ", ".join(cities)
print(joined)       # Delhi, Mumbai, Pune, Kolkata

