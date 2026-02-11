# a list can also be used to iteranate a list topple string or even a dictionary
name = "Furaha"

for letter in name:
    if letter == "r":
        print("the letter r")
else:
    print(letter)       

print("-------")
# below is a list of counties
counties = ["nairobi","mombasa","kajiado","ELDORET","MACHAKOS","MERU","EMBU"]
for county in counties:
    print(county)
print("---------")  
if "nairobi" in counties:
    print("nairobi is in the list of counties")
else:
    print("nairobi is not in the list of counties")    
print("==============")
# the far loop can also be used

player = {
    "name": "messi",
    "age": 25,
    "teams" : ["psg","barcelona","argentina"]
}
for key in player:
    print(key)
print("-------")    
for values in player:
    print(player["value"])
print("---------") 
# looop  throught the teams the player has played for
for teams in player ["teams"]:
    print(team)


