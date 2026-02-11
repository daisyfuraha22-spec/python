# on the try and except block: you can run some codes/statements and if it is successful the try block will get executed other than the except block will be executed when there is an anticipated error. 

try:
    number = 100
    answer = number/0
    print("the answer is",answer)
except Exception as e:
    print("there is an error :",e)    
