
answer = ""

def recurse(i, answer):
    if (i == n): 
        print(answer)
        return

    new_answer = ""
    for c in answer:
        new_answer += alphabet[i] + c
    new_answer += alphabet[i]

    recurse(i+1, new_answer)

#recurse(0, answer)

n = int(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"

def recurse2(i):
    if i+1==n: return alphabet[i] 
    answer = recurse2(i+1) + alphabet[i] + recurse2(i+1)
    return answer

result = recurse2(0)
print(result)

10 10 
**********
*..@....@*
*.@..@.@.*
*@...@.@.*
*@...@.@.*
*.@....@.*
*@...@.@.*
*@...@.@.*
*..@...@.*
**********