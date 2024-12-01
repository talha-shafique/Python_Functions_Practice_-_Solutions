def factorial(n):
    if n == 0 or n == 1:
        return 1
    else: 
        return n * factorial(n - 1)

# Example usage:
a=int(input('Enter a numbers: '))
print(f"The factorial of {a} is {factorial(a)}")