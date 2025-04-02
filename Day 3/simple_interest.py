# ptr/100

p = float(input("Enter principle: "))
t = float(input("Enter time: "))
r = float(input("Enter rate: "))

simple_interest = (p*t*r) / 100

# f string
print(f"The simple interest is {round(simple_interest, 2)}")
# format 
print("The simple interest is {}".format(round(simple_interest, 2)))
# %
print("The simple interest is %.3f" %simple_interest)
