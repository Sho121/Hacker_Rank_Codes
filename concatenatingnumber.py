#hackerrankcode
#concatenating two numbers without string implementation
import math
result=0
add=dict()
count=dict()
n=int(input("Enter the number: "))
if n==1000: #there was problem with counting the digits of the number 1000 so had to make an exception
    d=4
else:    
    d=(int(math.log(n,10)))+1 #counts the number of digits
for s in range(1,(d+1)):
    add[s]=0
i=1 
#storing i digit numbers to add{} and storing the no of i digit numbers to count{}   
while(i<=len(add)):
    c=0
    for j in range(1,n+1):
        if (j==1000):
            if((int(math.log(j,10)))+2)==i:
                add[i]=(add[i])*(pow(10,i))+j
                c=c+1
        elif((int(math.log(j,10)))+1)==i:
            add[i]=(add[i])*(pow(10,i))+j
            c=c+1
        else:
            continue
    count[i]=c 
    i=i+1
#producing the result while multiplyng (l+1) no. of zeros to value of add[l]   
for l in range(1,len(add)+1):
    result=(result*pow(10,l*count[l]))+add[l]
print(result)    
