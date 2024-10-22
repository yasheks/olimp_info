n=int(input())
m=int(input())
k=int(input())

def f(n,m,k):
f=1
while f:
if (k-1)<=min(n,m):
return min(n,m)*(max(m,n)-1)
if (k-1)<=max(n,m):
return max(n,m)*(min(m,n)-1)
if (k-1)>max(n,m):
if n==max(n,m):
m=m-1
else:
n=n-1
k=k-max(n,m)
elif (k-1)>min(n,m):
if n==min(n,m):
m=m-1
else:
n=n-1
k=k-min(n,m)

print(f(n,m,k))
