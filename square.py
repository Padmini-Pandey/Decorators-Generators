def show_info(func):
    def wrapper(*args,**kwargs):
        print("calling function..")
        func(*args,**kwargs)
        print("function executed")
    return wrapper
@show_info
def square(num):
    print(num*num)
a=int(input("enter a number "))
square(a)

