def weird_algorithm():
    n = int(input(""))
    print(n)

    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1
        print(int(n), end=" ")

def palindrome_reorder():
    string = input()
    letters = {}
    for s in string:
        if (s in letters):
            letters[s] = letters[s] + 1
        else:
            letters[s] = 1

    oddCount = 0
    center = ""
    first_half = ""

    for letter, count in letters.items():
        if count % 2 == 1:
            oddCount += 1
            center = letter * count 
        else:
            first_half += letter * (count//2)
    
    if oddCount > 1:
        print("NO SOLUTION")
        exit()

    second_half = first_half[::-1]
    print(first_half, center, second_half, sep="")

palindrome_reorder()
