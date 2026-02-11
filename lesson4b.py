# loops sometimes we may need to do a piece of work a number of reapeated times and such case scenarios we may use loops
#  a loop is a control sturucture that allows us to execute a block of code repeatedely until certain creditianls is met
# they are two types of lops in python i.e the for llop and the while loop
# below is the syntax of a for loop in python
"""
for variable in range(n)
    #the block of code to be executed

"""

for greeting in range(5):
    print("hello moses")
    
print ("--------------")
for number in range(10,70):
    print(number)
print("----------------")
for number in range(50,71,2):
    print(number)   

print("--------")    
# craeate a python program that prints odd numbers formm 100 to 150
for number in range(101,150,2):
    print(number)
print("----------")
# create a program that prints the miltples of three form 201 to 150
for number in range(201,149,-3):
    print(number)
print("-----------")
# create a python program that leaps years from 2000 to 2024
for year in range(2000,2025,4):
    print(year)






