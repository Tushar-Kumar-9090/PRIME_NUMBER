
## WAP to print every 2nd prime number in a given range 1-100 using while loop

n=1
count=0
while True:
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            count+=1
            if count%2==0:
                print(n)
    if n==100:
        break
    n+=1
