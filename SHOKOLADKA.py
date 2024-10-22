n = int(input())
m = int(input())
k = int(input())
n, m = (reversed(sorted([n, m])))
i = 1
j = max([j for j in range(1, m + 1) if i * j + k <= n * m + 1])
ans = i * j
flag = True
while i + j:
    if flag:
        i += 1
        flag = False
    else:
        j -= 1
    if i > n or j <= 0:
        break
    if i * j + k <= n * m + 1:
        flag = True
        if ans + k < i * j + k:
            ans = i * j
print(ans)
