n=int(input("enter any number :"))
i=2
while i<n:
    if n%i==0:
        break
        i=i+1
if i==n:
    print('num is prime')
else:
    print('num is not prime')
