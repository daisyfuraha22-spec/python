# tuple
# a tuple is an immtubale type of a list (it canot change)
# to introduce a tuple we use parenthisis

counties = ("nairobi","mombasa", "eldoret","kajaido","kisii")
print(counties)
print(type(counties))

# slicing
print(counties[3:])

# accesing items of a topple by use of the indexes
print(counties[5])
# note: below will genrate an error
# atrribute error
counties.append("machakos")
print(counties)
