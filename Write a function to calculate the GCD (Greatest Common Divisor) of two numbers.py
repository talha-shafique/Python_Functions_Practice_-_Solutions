def gcd(a, b):
    # Find the divisors of both numbers
    divisors_a = [i for i in range(1, a + 1) if a % i == 0]
    divisors_b = [i for i in range(1, b + 1) if b % i == 0]
    
    # Find common divisors
    common_divisors = set(divisors_a) & set(divisors_b)
    
    # Return the greatest common divisor
    return max(common_divisors)

num1 = 13
num2 = 48
gcd_result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gcd_result}")
