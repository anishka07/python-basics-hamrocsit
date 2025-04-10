m=input ("enter your word : ")
while m!="exit":
    print("enter your word: ")
print("exit")

# better code 

while True:
    user_input = input("Enter your word (or 'exit' to quit): ")
    if user_input.lower() == "exit":
        break
    else:
        print("You entered:", user_input)