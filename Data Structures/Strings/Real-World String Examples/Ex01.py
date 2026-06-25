# Data cleaning — the most common real use
# Messy data you get in real projects
names = ["  paras sharma ", "RAHUL VERMA", "priya SINGH  "]

clean_names = []
for name in names:
    cleaned = name.strip().title()
    clean_names.append(cleaned)

print(clean_names)