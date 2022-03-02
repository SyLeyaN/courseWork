import random

def rand(n):
        return random.randint(1,n)

def genstats(mas,masMode):
    for j in range(6):
        ch = []
        for i in range(4):
            ch.append(rand(6))
        m = min(ch)
        mas.append(sum(ch) - m)
        masMode.append((sum(ch) - m - 10) // 2)





