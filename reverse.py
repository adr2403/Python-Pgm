n=int(input("enter the number to be reversed"))
s=0
while n>0:
    i=int(n%10)
    s=(s*10)+i
    n=int(n/10)
print(s)      