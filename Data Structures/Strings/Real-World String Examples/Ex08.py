#WAP that counts how many vowels are in a given name.
#Ignore case — count both upper and lower vowels.

name = "Kurukshetra University"
vowels_count=0
for char in name:
    if char.lower() in "aeiouAEIOU":
        vowels_count+=1
print(f"Number of vowels in '{name}': {vowels_count}")