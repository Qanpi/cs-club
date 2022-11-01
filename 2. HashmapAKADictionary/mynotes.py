text = "How could we count how many times I said 'how' in this sentence?" #pay attention to the single and double quotes

words = text.split(" ")
frequencies = {}
print(words)

for w in words:
    w = w.lower()
    w = w.replace("?", "")
    w = w.replace("'", "")
    if w in frequencies:
        frequencies[w] += 1
    else:
        frequencies[w] = 1

print(frequencies)


# weird algorithm
def weird_algorithm():
    n = int(input())
    print(n)
    while (n != 1):
        if (n%2 == 0): 
            n /= 2
        else:
            n = n*3 + 1
        print(int(n), end=" ")

weird_algorithm()
