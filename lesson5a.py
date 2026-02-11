# python functions
# they are block of code that performs a given task .they can be reused through out the program to perform diffrent tasks.
# functions are defined using the def keyword. (deifne)
# we have two main types of functions i.e
# inbuilt functions > they come preinstalled with the interprete i.e print(),pop,range
# ,append
# user defined functions- they are created by a programmer to solve a given task
# to define a function you need to give it a name followed by parenthesis()
# for the function body it is usually indented and to invoke a function we use the function name



def greetings():
    print("hello how are you")

# below we call the function by use of its name
greetings()   

print("------------------")
# addition function
def addition():
    num1 = 40
    num2 = 50
    sum = num1 + num2
    print("the sum of the numbers is ",sum)
addition()
print("================")
# create a function  that is able to multiply three values
def multiplication():
    num1 = 10
    num2 = 60
    num3 = 5
    product = num1 * num2 *num3
    print("the product of the numbers is:",product)

multiplication()
print("--------------")
# below is a division function
def divide():
    number1 = int(input("enter the first number:"))
    number2 = int(input("enter the second number:"))
    quotient = number1 % number2
    print("the number is:"<quotient)
    print("-----------")

for function in range(3):  
    divide()   

    