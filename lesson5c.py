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

