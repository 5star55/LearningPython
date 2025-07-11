n= int(input("Enter number of numbers in fibonacci series: "))

def fibonacci(n):
    a,b=0,1
    for x in range(n):
        print(a, end=' ')
        a,b=b,a+b

fibonacci(n)
