ankit= int(input("age of ankit ? "))
anurag= int(input("age of anurag ? "))
mohan= int(input("age of mohan ? "))
if (ankit>anurag and ankit>mohan):
   print ("ankit is oldest")
elif (ankit<anurag and ankit<mohan):
   print ("ankit is youngest")
elif (anurag>ankit and anurag>mohan):
    print ("anurag is oldest")
elif (anurag<ankit and anurag<mohan):
    print ("anurag is youngest")
elif (mohan>ankit and mohan>anurag):
    print ("mohan is oldest")
elif(mohan<anurag and mohan<anki):
     print ("mohan is youngest")
else :
    print ("there age are not unequal")
