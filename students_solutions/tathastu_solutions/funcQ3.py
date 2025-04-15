# 3. Write a function to find the factorial of a number.

def factorial_number(facto):
    result = 1
    for i in range(1, facto  + 1):
        result *= i
    return result

answer = factorial_number(9)
print(f"factorial is {answer}")