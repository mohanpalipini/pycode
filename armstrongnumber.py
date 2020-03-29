n = int(input("enter the number:"))
s=0
while n!=0:
    m=n%10
    s=s+m**3
    n=n//10


    
if n == s:
    print(n,s,"armstrong milgaya")
else:
    print(n,s,"oh no  we failed")

print(s)
