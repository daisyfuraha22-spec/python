# create a python program that is able to determine whether the number is an odd number or an even number
# if number % 2==0:
#     print("the number is odd")
# else:
#     print("the number is even") 
# create a python program  that is able to determine whetther a persorn can donate blood based on age and 
# if the wight is greater than 50 kgs and wight is above 18 you can be able to donate blood else not possible
age = int(input("enter age:"))
weight = float(input("enter weight:"))

if age >=18 and weight > 50:
    print("can donate")
else:
    print("not possible")    
