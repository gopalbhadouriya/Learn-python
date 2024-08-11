friends = ["Rohan","Raghav","Mango",6,784.45,False,"Akasha"]
friends[0] = "MR.Gopal ji" # we change string 
print(friends[0])
print(friends)
friends.append("RUSTAM") # this change list

print(friends)
#  we know that string can not be change but in "list" case string can  change able as upper example
# string are immutable but list is mutable
friends[6] = "MANU"
print(friends[6])
friend = ["manu"]
friend[:] = "Manu"
print(friend[:])
caracter = friend[0]
print(caracter)
name = "Rustam is a good boy"
print(name.find("good"))
# find function is only work in string not in list
print(friends[1:5])





