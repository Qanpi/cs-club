#DISCLAIMER: do not worry if you don't entirely get this topic, it's partly due to it's nature and partly due
#my rugged explanations :). It will come with practice, if you wish to practice it.

alphabet = "abcdefghijklmnopqrstuvwxyz"
n = int(input())

#silly me realized you can rewrite the first solution as simply iterative (using iteration = for loop)
def iterative_solution(n):
    i = 0
    answer = ""

    while (i < n):
        new_answer = ""

        for c in answer:
            new_answer += alphabet[i] + c

        new_answer += alphabet[i]
        answer = new_answer

        i+=1
    
    print(answer)


iterative_solution(n)

def recursive_solution(i):
    if i+1==n: return alphabet[i] 
    answer = recursive_solution(i+1) + alphabet[i] + recursive_solution(i+1)
    return answer

answer = recursive_solution(0)
print(answer)


