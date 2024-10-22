s = int(input())  
n = int(input())  
a = [(z[::-1]) for z in enumerate([int(input()) for i in range(n)], 1)]
f = s  
u = 0  

for j in range(len(a)):
    e, i = a[j] 
    if i > f and a[j][0] >= 0: 
        break
    elif i > f and e <= 0: 
        continue
 
    (u, f) = (a[j][1], f + e) if f + a[j][0] >= f else (u, f) 

print((f - n - 1) % (f - n))
