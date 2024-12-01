def find_largest(numbers):
    return max(numbers)  

# Example usage:
numbers = input("Enter a list of numbers (separated by spaces): ").split()
numbers = [int(num) for num in numbers] 
print(f"The largest number in the list is: {find_largest(numbers)}")
