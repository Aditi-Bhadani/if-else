a=int(input("Enter the age of ankit: "))
b=int(input("Enter the age of anurag: "))
c=int(input("Enter the age of mohan: "))

if(a>b and a>c):
    print("ankit is elder")
elif(b>a and b>c):
    print("anurag is elder")
else:
    print("mohan is elder")

if(a<b and a<c):
    print("ankit is youngest")
elif(b<a and b<c):
    print("anurag is youngest")
else:
    print("mohan is youngest")
