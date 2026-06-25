# Given a list of phone numbers, check if each is valid. A valid Indian mobile number has exactly 10 digits, is numeric, and starts with 6, 7, 8, or 9.

phones = ["9876543210","123","8800abc123","7011223344","5123456789","6999988877"]

for num in phones:
    if len(num)==10 and num.isnumeric() and num[0] in "6789":
        print(f"{num} → Valid")
    else:
        print(f"{num} → Invalid")