# You receive raw train data as strings.
# Extract train number, name, and departure time from each entry and print a clean formatted report.

trains = [
    "12301|Rajdhani Express|06:00|NewDelhi",
    "12259|Duronto Express|14:30|Mumbai",
    "22691|Rajdhani Express|21:00|Bengaluru",
]
print("-" * 70)
print(f"{'Train No':<10} {'Train Name':<20} {'Time':<10} {'Station':<15}")
print("-" * 70)

for train in trains:
    parts = train.split("|")
    train_no = parts[0]
    train_name = parts[1]
    departure_time = parts[2]
    station = parts[3]

    print(f"{train_no:<10} {train_name:<20} {departure_time:<10} {station:<15}")

print("-" * 70)