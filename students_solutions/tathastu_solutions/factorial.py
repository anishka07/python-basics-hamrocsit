
# 2. Write a while loop to calculate the factorial of a given number (e.g., 5).

num =int(input("enter the number : "))
fact = 1
i = 1
while i<= num:
    fact *= i
    i += 1

print(f"factorial number : {fact}")
