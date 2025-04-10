"""WAP to find the grade of the student based on the marks """
# 1 user asks for marks as an input and your program should be able to grade the student based on the marks they got

# 2 if the marks are greater than or equal to 90, the grade should be A
# 3 if the marks are greater than or equal to 80, the grade should be B
# 4 if the marks are greater than or equal to 70, the grade should be C
# 5 if the marks are greater than or equal to 60, the grade should be D

marks = float(input('enter the marks: '))
if marks >= 90:
    print('The grade is A.')
elif marks >= 80:
    print('The grade is B.')
elif marks >= 70: 
    print(' The grade is C.')
else:
    print('The grade is D.')
