# File handling = reading from and writing to files (like .txt, .csv).
# It lets our code work with data stored on disk instead of only in variables in memory.

# Opening a file

f = open("example.txt", "r")   # open for reading
# ... do something ...
f.close()

# Common modes:

    # "r" → read (file must exist).
    # "w" → write (create or overwrite).
    # "a" → append (add to end).
    # "x" → create new file (error if already exists)

# Reading from a file

f = open("example.txt", "r")
content = f.read()        # whole file as one string
f.close()

# Other methods:

    # read() → whole file as string.
    # readline() → one line at a time.
    # readlines() → list of all lines.

# Example:

f = open("example.txt", "r")
for line in f:
    print(line.strip())
f.close()

# Writing to a file

f = open("output.txt", "w")  # overwrite or create
f.write("Hello world\n")
f.write("This is a new line\n")
f.close()

# Append instead:

f = open("output.txt", "a")  # add to existing content
f.write("Another line\n")
f.close()

# The with statement 
# with automatically closes the file, even if an error happens.

with open("example.txt", "r") as f:
    content = f.read()
    print(content)   # file auto-closed after this block