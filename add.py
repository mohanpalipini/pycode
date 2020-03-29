void add(a,b):
    if(a!=b):
        return ((a*a-b*b)/(a-b))
    else:
        return 2*a
void main():
    a=int(input("first:"))
    b=int(input("second:"))
    print(add(a,b))
main()
