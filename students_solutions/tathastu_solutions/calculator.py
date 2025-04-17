# use functions to make a fully functional calculator, each function should be a different operation (add, subtract, multiply, divide). if the user chooses 1, add, if the user chooses 2, subtract, etc.
# make sure to use functions and not just a big if else statement

#function definition
# def add(a, b):
#     return (a + b)

# def subract(a,b):
#     return(a - b)


# def multiply(a, b):
#     return(a*b)

# def division(a, b):
#     if a == 0:
#         return"error"
#     else:
#         return(a/b)

# #function for calculator 
# def calculator():
#     print("what do you want to perform: ")

#     print("1. add")
#     print("2. subract")
#     print("3. multiply")
#     print("4. divisiom")

#  # asking user what to perform  
# calculate = input("Enter your choice (!/2/3/4): ")

# # asking numebr with user
# n1 = float(input("Enter the first number: "))
# n2 =float(input("Enter the sceond number: "))

# if calculate =="1":
#     print(f"{n1} + {n2} = {add(n1, n2)}")
# elif calculate == "2":
#     print(f"{n1} - {n2} = {subract(n1, n2)}")
# elif calculate == "3":
#     print(f"{n1} * {n2} = {multiply(n1, n2)}")
# elif calculate == "4":
#     print(f"{n1} / {n2} = {division(n1, n2)}")
# else:
#     print("Error")

#run program
# calculator()


# better code 
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cant divide by zero"
    return a / b 


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
while True:
    choice = input("Enter 1 for add, 2 for sub, 3 for mul, 4 for div and 'exit' to quit: ")
    if choice == 1:
        add_ans = add(num1, num2)
        print(f"The sum for the numbers is: {add_ans}")
    elif choice == 2:
        sub_ans = sub(num1, num2)
        print(f"The difference for the given number is: {sub_ans}")
    elif choice == 3:
        mul_ans = mul(num1, num2)
        print(f"The product for the given numbers is: {mul_ans}")
    elif choice == 4:
        div_ans = div(num1, num2)
        print(f"The division for the given numbers is: {div_ans}")
    elif choice == "exit":
        print("Exiting")
        break
