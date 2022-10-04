n=int(input("no.of terms :"))
n1,n2=0,1
c=0
if n<=0:
    print("enter value greater than 0")
elif n==1:
    print(n1)
else :
    print("your sequence is:")
    while c < n :
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        c=c+1