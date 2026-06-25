# Given a paragraph, count how many times each word appears.
# Ignore case and punctuation (remove . , ! ?). Print words that appear more than once, sorted by count.

text = "Data is the new oil. Data drives decisions. Good data is clean data."

clean = text.lower()
for ch in [".", ",", "!", "?"]:
    clean = clean.replace(ch, "")

words = clean.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

for word, count in freq.items():
    if count > 1:
        print(f"{word:<6}: {count}")