from re import L


def candy():
    n = int(input())
    a = int(input())
    b = int(input())

    cheapest = min(a, b)
    max_candy = n // cheapest
    print(max_candy)

n = 0
alphabet = "abcdefghijklmnopqrstuvwxyz"

def string():
    global n
    n = int(input())

    #recurse(0, "")
    answer = recurse2(0)
    print(answer)

def recurse(i, answer):

    if i == n: 
        print(answer) 
        return
    
    new_answer = ""

    for c in answer:
        new_answer += (alphabet[i] + c)
    new_answer += alphabet[i]

    recurse(i+1, new_answer)

def recurse2(i):
    if i==n-1: return alphabet[i]
    answer = recurse2(i+1) + alphabet[i] + recurse2(i+1)
    return answer

string()






