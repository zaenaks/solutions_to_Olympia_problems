def mirror_prime(a, b):
    res = 0
    for i in range(a, b+1):
        per = 0
        num2 = str(i)[::-1]
        num2 = int(num2)
        if num2 > i:
            d = num2
        else:
            d = i
        for j in range(2, d//2+1):
            if num2 % j != 0 and i % j != 0 or j == num2 or j == i:
                per += 1
            else:
                break
        if per == d//2 - 1:
            res += 1
    return res


ls = list(map(int, input().split()))
print(mirror_prime(ls[0], ls[1]))
