# python lists
# a list in python is a colectioon of items that are orderded in a certain way.
# a list is introduced by the use o the square brackets {}
# the items of a lsit are started inside of indexes. note: in programming we start counting from index zero
# bmw.benz, mercedes,porshe..
# a list is mutable which menas it can be changed.

cars = ["bmw" ,"benz","hiance","prado","probox","mclaren","mercedes"]

print(cars)
print(type(cars))

# accessing items of a list
print(cars[2])
print("the car on index four is",cars[4])

cars.pop()

# list slicing - this is the creating a list from a given bigger list.
print(cars[4:])

# printing form index zero index to three
print(cars[:4])

# printing from hiance to probox
print(cars[2:5])

# list - mutability
# we use the functiion to add an item at the end of the list
cars.append("range")
print(cars)
cars.append("subaru")
print(cars)

# we sue the pop function to remove an item at the nd of the list.
cars.pop()
print(cars)

# we can use an index to add items to a list
cars[5] = "pajero"
print(cars)


# we can use the sort function to sort out our tiems in alphabetical order
cars.sort(reverse=True)
print(cars)



