#A string is a sequence of characters.
# It is immutable — you cannot change a string in place, you can only create a new one.

# We can primarily write a string in these three ways. 
a ='paras'       # Single quoted string 
b = "paras"      # Double quoted string 
c = '''paras'''  # Triple quoted string 

s1 = "Hello"
s2 = 'Data Analyst'
s3 = "12345"   # still a string, not a number

# Indexing — accessing one character

name = "Paras"
#        P  a  r  a  s
# index:  0  1  2  3  4
# neg:   -5 -4 -3 -2 -1

print(type(name))          # <class 'str'>
print(name[0])              # P
print(name[1])              # a
print(name[-1])             # s  (last character)
print(name[-2])             # a  (second last)

# Slicing — accessing a range of characters

# string[start:stop:step]

s = "Data Analyst"
#     0123456789...

print(s[0:4])               # Data
print(s[5:])                # Analyst (5 to end)
print(s[:4])                # Data (start to 4)
print(s[-7:])               # Analyst (last 7)
print(s[::2])               # Dt nls (every 2nd)
print(s[::-1])              # tsylanA ataD (reversed)

# Real use — extract parts of data
date = "2024-06-25"
year  = date[0:4]           # 2024
month = date[5:7]           # 06
day   = date[8:10]          # 25
print(year, month, day)

# concatenation
#"hello"+"world"="helloworld"
str1="hello"
str2="world"
final_str=str1+str2
print(final_str)