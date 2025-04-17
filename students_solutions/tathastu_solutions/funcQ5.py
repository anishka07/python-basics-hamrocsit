# 5. Write a function to reverse a string.

def reverse_string(revstr):
    reversed_str = revstr[::-1]
    return reversed_str

retunstring = reverse_string("pikachu")

print(retunstring)

# better code 

def reverse_string(word):
    return word[::-1]


user_word = str(input("Enter a word: "))
print(f"The reverse of the intered string is: {reverse_string(user_word)}")