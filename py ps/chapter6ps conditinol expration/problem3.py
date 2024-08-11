a = ('make a lot of money')
b = ('buy now ')
c = ('click here')
message = input('enter a comment here : ')
if((a in message) or (b in message) or (c in message)):
    print("spam detected")
else:
    print("not detected") 