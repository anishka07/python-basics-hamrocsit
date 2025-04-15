# use functions to make a fully functional calculator, each function should be a different operation (add, subtract, multiply, divide). if the user chooses 1, add, if the user chooses 2, subtract, etc.
# make sure to use functions and not just a big if else statement

#function definition
def add(a, b):
    return (a + b)

def subract(a,b):
    return(a - b)


def multiply(a, b):
    return(a*b)

def division(a, b):
    if a == 0:
        return"error"
    else:
        return(a/b)

#function for calculator 
def calculator():
    print("what do you want to perform: ")

    print("1. add")
    print("2. subract")
    print("3. multiply")
    print("4. divisiom")

 # asking user what to perform  
calculate = input("Enter your choice (!/2/3/4): ")

# asking numebr with user
n1 = float(input("Enter the first number: "))
n2 =float(input("Enter the sceond number: "))

if calculate =="1":
    print(f"{n1} + {n2} = {add(n1, n2)}")
elif calculate == "2":
    print(f"{n1} - {n2} = {subract(n1, n2)}")
elif calculate == "3":
    print(f"{n1} * {n2} = {multiply(n1, n2)}")
elif calculate == "4":
    print(f"{n1} / {n2} = {division(n1, n2)}")
else:
    print("Error")

#run program
    calculator()