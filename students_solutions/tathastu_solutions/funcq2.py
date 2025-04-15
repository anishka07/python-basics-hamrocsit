# 2. Write a function to check if a number is even or odd.

def odd_even(n):
 if n % 2 == 0:
  return "even "
 else:
  return "odd"
ans = odd_even(11)
print(f"the number is {ans}")