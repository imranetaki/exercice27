n=int(input("entrer la valeur de n svp "))
while n<= 0:
    n=int(input("entrer la valeur de n"))
print("les diviseurs sont : ")
for i in range (1,n+1) :
    if (n%i==0) : 
        print (i,end=" ")