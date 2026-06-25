# Validation — checking if data is correct
# Check if a phone number looks valid
phones = ["9876543210", "123", "98765abc10", "8800112233"]

for phone in phones:
    if len(phone) == 10 and phone.isnumeric():
        print(f"{phone} → Valid")
    else:
        print(f"{phone} → Invalid")