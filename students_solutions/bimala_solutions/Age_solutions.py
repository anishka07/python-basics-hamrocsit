'''WAP to check if a user is eligible to vote or not'''
# Ask for the age, legal age to vote is 18
age = int(input('enter the age:'))
if age >= 18: 
    print('You are eligible to vote.')
else:
    print('You are not eligible to vote.')