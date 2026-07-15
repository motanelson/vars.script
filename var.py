import os
def finds(l:list,keys:str):
    for ll in l:
        if ll[0]==keys.strip():
            return ll[1]
    return -1
def findse(l:list,keys:str,values:str):
    for ll in l:
        if ll[0]==keys.strip():
            ll[1]=values
            return l
    l.append([keys,values])
    return l

print("\033c\033[47;30m\nget me a .var varscript file to view")
a=input().strip()
f1=open(a,"r")
ff=f1.read()
f1.close()
fff=ff.split("\n")
vars=[["print",""],["input",""]]
for b in fff:
    b=b.strip()
    
    if b!="":
        bb=b.split("=")
        if len(bb)==1:
            bb[0]=bb[0].strip()
            bb[0]=bb[0].lower()
            if bb[0]=="print":
                print(finds(vars,"print"))
            elif bb[0]=="input":
                a=input().strip()
                vars=findse(vars,"input",a)
            elif bb[0]=="debug":
                print(vars)
            elif bb[0]=="exit":
                exit(0)

        elif len(bb)>1:
            bb[0]=bb[0].strip()
            bb[0]=bb[0].lower()
            vars.sort()
            for dd in vars:
               bb[1]=bb[1].replace("$"+dd[0]+" ",dd[1])
            vars=findse(vars,bb[0],bb[1])

 