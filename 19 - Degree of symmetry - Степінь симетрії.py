def step(N):
    res = 0
    if len(N) % 2 == 1:
        res += 1
    for i in range(len(N)//2):
        if N[i] == N[i * (-1) - 1]:
            res += 1
    return res


print(step(input()))
