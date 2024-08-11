# this is dictonary
mark = {
    "Rustam" : 100,
    "kartik" : 85,
    "shubam" : 43,
    0 : "Dinesh"

}

# .items it make an tuple in turminal
print(mark.items())
#  .keys it show keys as tuple in terminal
print(mark.keys())
# for value in terminal use .values
print(mark.values())
#  to update dict use .update
mark.update({"Ram" : 99}) # dict is always in {}
# it  will add ram into dict
print(mark) # dict are mutable it change list
#  and change a word
mark.update({"Kartik" : 95})
print(mark) # this update kartik value
#  to get any str or int value use .get
print(mark.get("Rustam"))
# it get value of Rustam
# important fact
# diifrence bitween 
# print(mark.get("Rustam")) if we enter an unkown value we get none
# print(mark["Rustam"]) if we enter an unkown value we get error
# ex---
# print(mark.get("Rustam2")) # there is no element rustam2
# print(mark["Rustam2"]) # this is showing error
# .len
dv = {0:"kh",1:"hgfh",2 :"gj"}
# it return 3 becouse it store 3 element


print(len(dv))













