
## WAP to print 1st 10th prime number using for loop???


n = 2
count = 0
while True:
    i = 2
    c=0
    if n>3:
        while i<(n//2+1):
            if n%i==0:
                break
            else:
                c+=1
            if c>=2:
                break
            else:
                print(n)
                count+=1
            i+=1
    else:
        print(n)
        count+=1

    if count == 10:
        break
    n+=1
