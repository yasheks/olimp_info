n=int(input())
a=int(input())
x=int(input())
b=int(input())
y=int(input())
ax=1+2*x
by=1+2*y
if n<ax*a+by*b:
    if x>y:
        ind=0
        for i in range(a):
            ind+=(x+1+x)
            if ind-x>=n:
                print(ind-x,x)
                exit()
            print(ind-x, x)
        for j in range(b):
            ind+=(y+1+y)
            if ind-y>=n:
                print(ind-y,y)
                exit()
            print(ind-y,y)
    else:
        ind=0
        for i in range(b):
            ind+=(y+1+y)
            if ind-y>=n:
                print(ind-y,y)
                exit()
            print(ind-y,y)
        for j in range(a):
            ind+=(x+1+x)
            if ind-x>=n:
                print(ind-x,x)
                exit()
            print(ind-x, x)
        
else:
    print(-1)
    
