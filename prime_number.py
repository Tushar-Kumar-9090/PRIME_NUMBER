n = int(input("Enter The Number: "))
if n>1:
    for i in range(2,n//2+1):
        if n%i==0:
            print("Not Prime Number")
            break
    else:
        print("Prime Number")
else:
    print("Not Prime Number")