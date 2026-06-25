# Given a sentence, reverse each individual word but keep the word order the same.

sentence = "Data Analyst Job Delhi"

for word in sentence.split():
    reversed_word=word[::-1]
    print(reversed_word, end=" ")