n=int(input("\n Enter a number:-"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if (i==1 or j==1 or i==n or j==i):
            print("*",end="")
        else:
            print(" ",end="")
    print()
