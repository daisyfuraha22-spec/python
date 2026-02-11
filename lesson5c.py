# test one
# by use of a function that accepts. parameters,calculate the simple intrrest given principal as 45000,rate is% and the time taken s 8 years.(si = p *r *t /100)
# use the same function inside of a loop to calculate two other simple intrests. note use your own principal,rate and time.
def simpleintrest(principal,rate,time):
    simpleintrest = principal *rate *time/100
    return simpleintrest
# firstcalc
principal = 45000
rate = 5
time = 8
result1 = simpleintrest(principal,rate,time)
print("simpleintrest1",result1)



values = [
    (2000,4,5)
    (6000,6,3)
]
for p,r,t in values:
    result = simpleintrest(p,r,t)
    print("simpleintrest",result)
print("--------------------")
# question one
def arearectangle():
    length = 10
    width = 5
    area = length  * width
    print("area of a rectangle",area)
arearectangle() 

print("-----------")

# question two
def calculate(x,y)
    sum = x + y
    difference = x - y
    product = x * y
    division = x % y
    return sum,difference,product,division
result = calculate (10,5)

print("sum:",result[0])
print("diffrence:",result[1])
print("product:",result[2])
print("division",result[3])

print("======================")

# question three
def checknumber():
    num = int(input("enter a number"))
    if num > 0:
        print("positive")
    elif num < 0:
        print ("negative")
    else:
        print ("zero")  
checknumber()

print("-----------------------------")

# question four
def sumnumbers(n):
    total = 0
  for i in range(1, n + 1):
    total += i
    print ("sumfrom 1 to",n,"is:",total) 
sumnumbers(5) 

print("-----------------------")

# question five
def squarenumbers()
    n = int(input("enter a number"))
    i = 1
  while i <=n:
    print("squareof",i,"is",i*i)  
    i += 1
squarenumbers()    


        
