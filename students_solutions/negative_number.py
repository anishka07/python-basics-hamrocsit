# 4. Write a while loop that keeps asking the user for a number until they enter a negative number.

num = int(input("enter the number : "))
while num >= 0:
    num= int(input("enter the number : "))


print("end")

# better code 

while True:
    number = int(input("Enter a number (negative to stop): "))
    if number < 0:
        break
    print(f"You entered: {number}")
    