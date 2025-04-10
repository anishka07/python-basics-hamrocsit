
# 4. Write a while loop that keeps asking the user for input until they type "exit".
a= input("enter the input : ")
while a != "exit":
    a = input("enter the input : ")

print(" exit")


# better code 
while True:
    user_input = input("Enter something (type 'exit' to quit): ")
    if user_input.lower() == "exit":
        print("Exiting the loop.")
        break
    else:
        print(f"You entered: {user_input}")
        