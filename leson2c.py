# a dictionary is a data type that stores data in terms of key- value pair 
# a dictionary is introduced by the use of curly braces{}
#  the values stored inside a dictionary can be of any data type
#  to acces the values in a dictionary we use the keys

phonebook = {
    "Furaha:": "2547689056",
    "Mary": "254678905"
}
# showing the entire dictionary
print(phonebook)
print(type(phonebook))

# print out bensons number
print(phonebook["Furaha"])

player = {
    "name": "messi",
    "age":40,
    "teams":["psg","barcelona","argetina"]
    "more" : {
        "children" : 3,
        "residence" : "US",
        "phone" :(2546789076543,254356789,2546789045)
    }

}
print("messis second number ",player["more"]["phone"][1])
# print barcelona - the second team 
print(player["teams"][1])
print(player["teams"])
print("messis second number ",player["more"]["phone"][1])
