def double_result(func):
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        return result*2
    return wrapper
@double_result
def add(a,b):
    return a+b
m=int(input("enter a number "))
n=int(input("enter a number "))
print(add(m,n))
