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
# refactor code above into main function

# ABC
# AAC
# ABAB

# palindrome reorder
def palindromize():
    string  = input()
    letters = {}

    # convert to dict
    for s in string:
        if (s in letters):
            letters[s] += 1
        else:
            letters[s] = 1
    
    oddCount = 0 # could have as boolean, right?
    first_half = ""
    center = ""
    for letter, count in letters.items(): # go through items, keys and value
        # letter = pair[0]
        # count = pair[1]
        if (count % 2 == 1):
            oddCount += 1
            center = letter * count #* l[1], go through what * means in the context of strings in Python
        else:
            first_half += letter * (count//2) # explain what // means

    second_half = first_half[::-1] # go through string slicing
    if (oddCount > 1): print("NO SOLUTION") #ABC
    else: 
        print(first_half, center, second_half, sep="")
    # we notice that the below two cases are the same if oddCount has been 0

    # elif (oddCount == 1):
    #     print(first_half, center, second_half, sep="")
    # else:
    #     print(first_half, second_half, sep="")


palindromize()
