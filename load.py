def printxyzt(values):
    print("x,y,z,time="+str(values))

def printv(a):
    for aa in a:
        printxyzt(aa)

def build(lena,incx,incy,incz,inct):
    x=0
    y=0
    z=0
    t=0
    list1=[]
    for n in range(lena):
        l1=[x,y,z,t]
        list1=list1+[l1]
        x=x+incx
        y=y+incy
        z=z+incz
        t=t+inct
    return list1 
def saves(names,list1):
    f1=open(names,"w")
    for n in list1:
        x,y,z,t=n
        f1.write(str(x)+", "+str(y)+", "+str(z)+", "+str(t)+"\n")
    f1.close()
def loads(names):
    x=0
    y=0
    z=0
    t=0
    list1=[]
    f1=open(names,"r")
    s=f1.read()
    f1.close
    list2=s.split("\n")
    for n in list2:
        n=n.strip()
        if n!="":
            nn=n.split(",")
            x=int(nn[0].strip())
            y=int(nn[1].strip())
            z=int(nn[2].strip())
            t=int(nn[3].strip())
            list1=list1+[[x,y,z,t]]
    return list1

print("\033c\033[43;30m\n")
aaa=loads("data.csv")
printv(aaa)
