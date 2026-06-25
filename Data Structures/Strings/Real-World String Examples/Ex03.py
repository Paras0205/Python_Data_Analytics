# Extract year from date column
dates = ["2024-01-15", "2023-11-30", "2024-06-25"]

for date in dates:
    year = date[:4]
    month = date[5:7]
    print(f"Year: {year}, Month: {month}")