#num=5
#print("Factorial of 5 =" , fact(num))

def fact(x):
    if x==1:
        return
    else:
        return(x*fact(x-1))