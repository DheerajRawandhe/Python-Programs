def printmultiple(n):
    i=1
    while i<=10:
        print(n*i,end="\t")
        i=i+1
        print()
    i=1
    while i<=10:
        printmultiple(i)
        i=i+1
    
