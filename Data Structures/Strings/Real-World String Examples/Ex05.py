# Given this messy list, clean every city name: strip spaces, convert to title case, remove duplicates.

cities = ["  delhi", "MUMBAI ", " pune", "delhi  ", "Bengaluru", " MUMBAI"]

cleaned_cities=[]
for city in cities:
    cleaned=city.strip().title()
    if cleaned not in cleaned_cities:
        cleaned_cities.append(cleaned)
print(cleaned_cities)