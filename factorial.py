#factorial using for loop

def factorial(n):
    num=1
    for i in range(1,n+1):
        num*=i
    return num

print(factorial(5))

# factorial using function

def factorial_(n):
    if n==0:
        return 1
    
    return n* factorial(n-1)
print(factorial_(5))
