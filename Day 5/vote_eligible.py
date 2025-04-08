'''WAP to check if a user is eligible to vote or not'''
# Ask for the age, legal age to vote is 18


vote_age = float(input('Enter the age '))

if vote_age >= 18:
    print("You are elligibe for voting")
else:
    print("You are not elligible for voting")