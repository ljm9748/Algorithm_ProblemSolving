def factorial(num):
    if num <= 1:
        return 1
    else:
        return factorial(num-1)*num
N=int(input())
print(factorial(N))
