# 1. Write a for loop to print the even numbers from 2 to 20.
for i in range (2, 21, 2):
    print(i)


# another way 
for i in range(2, 21):
    if i % 2 == 0:
        print(i)