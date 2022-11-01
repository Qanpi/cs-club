text = "How could we count how many times I said 'how' in this sentence we?"

words = text.split(" ")
print(words)
frequencies = {}

for w in words:
    w = w.lower()
    w = w.replace("?", "")
    w = w.replace("'", "")
    if w in frequencies:
        frequencies[w] += 1
    else: 
        frequencies[w] = 1

print(frequencies)