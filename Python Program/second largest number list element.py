list=[900,10,20,4,45,99,1000]
print("\n")
print("\n List Element =",list)
mx=max(list[0],list[1])
secondmax=min(list[0],list[1])
n=len(list)
for i in range(2,n):
    if list[i]>mx:
        secondmax=mx
        mx=list[i]
    elif list[i]>secondmax and \
         mx !=list[i] :
             secondmax=list[i]
    elif mx==secondmax and \
         secondmax !=list[i] :
             secondmax=list[i]
print("\n The Second Largest Number Is:- ",\
      str(secondmax))
             
        
        
