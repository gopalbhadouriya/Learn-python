n = int(input('Enter your number: '))

for i in range(2,n):
    if(n%i) == 0:
        print("Yes,this is not prime number")
        break
else:
    print("NO,this is a prime number")



