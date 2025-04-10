# 4. Write a while loop that keeps asking the user for input until they type "exit".
while True:
    user = input("Enter your message: ")
    print(user)
    if user.lower() == "exit":
        break
