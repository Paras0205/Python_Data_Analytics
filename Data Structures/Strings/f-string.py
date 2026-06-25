#f-strings are the best way to put variables inside text.
# Put f before the quote, then use {} around any variable or expression.

name = "Paras"
cgpa = 8.5
city = "Delhi"

# Basic usage
print(f"My name is {name}")
print(f"CGPA: {cgpa}, City: {city}")

# Expressions inside {}
marks = [85, 90, 78, 92]
print(f"Average: {sum(marks)/len(marks)}")  # 86.25

# Formatting numbers
salary = 450000
print(f"Salary: ₹{salary:,}")              # ₹4,50,000
print(f"CGPA: {cgpa:.2f}")                 # 8.50
print(f"Percentage: {85.678:.1f}%")        # 85.7%

# Padding and alignment
for s in ["Paras", "Rahul", "Priya"]:
    print(f"{s:<10} | Passed")