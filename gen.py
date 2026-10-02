def countdown(n):
    while n>0:
        yield n
        n=n-1
a=int(input("enter a number "))
g=countdown(a)
for j in g:
    print(j)