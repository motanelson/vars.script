def printxyzt(values):
    print("x,y,z,time="+str(values))

def printv(a):
    for aa in a:
        printxyzt(aa)

print("\033c\033[43;30m\n")
aaa=[[0,1,0,0],[1,0,1,0],[0,0,0,1],[1,1,1,0]]

printv(aaa)
