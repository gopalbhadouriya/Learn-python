# this is dictonary
mark = {
    "Rustam" : 100,
    "kartik" : 85,
    "shubam" : 43,

}

print(mark,type(mark))
# when we use() this is tuple
# when use [] this is a list
# when use {} this is a dictonary
#  to print some thing value and dict
#  dict are used in : (colin)
# ex ---
print(mark["Rustam"])
# this will print Rustam element value
# how to use it 
# fist print valuse and type in[]
# a element name 
print(mark["kartik"])
print(mark["shubam"])


# pop uses to remove some thing

# Create a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(type(my_dict))

# Remove and return value for key
removed_value = my_dict.pop('b', 'not found')
print("Removed value for key 'b':", removed_value)
print("Dictionary after pop():", my_dict)

# Attempt to pop a non-existent key
removed_value = my_dict.pop('d', 'not found')
print("Removed value for key 'd':", removed_value)

# 
dic4 = {"Rustam" : 100,"Kartik" :85 ,"KK" :34}


remove = dic4.pop("KK","not found")

print(f"remove value {remove}")
print("dict after pop",dic4)

remove = dic4.pop("KK","not found")
print("removed value for key 'KK'",remove)


























