a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,4):
    for j in range(0,4):
        for k in range(0,4):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])
                break;
