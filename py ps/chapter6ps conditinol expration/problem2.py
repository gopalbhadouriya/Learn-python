a = int(input("enter sub1 mark : "))
b = int(input("enter sub2 mark : "))
c = int(input("enter sub3 mark : "))


total_percantage = (100)*(a+b+c)/300
if(total_percantage== 100):
    print("super great")
if(total_percantage>= 40 and a>=33 and b>=33 and c>=33):
    print('you are passed',"your percantage is :",total_percantage)

else:
    print("you are foolish")
    print('you are failed',"your percantage is :",total_percantage)

