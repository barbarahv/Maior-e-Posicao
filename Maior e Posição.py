j=0
loc=0
for i in range(100):
    n=int(input())
    if(n>j):
        j=n
        loc=i
print(j)
print(loc+1)



x=[]
for i in range(100):x.append(int(input()))
print(f"{max(x)}\n{x.index(max(x))+1}")