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
print("\033c\033[43;30m\n")
aaa=build(20,5,4,2,1)
printv(aaa)
saves("data.csv",aaa)