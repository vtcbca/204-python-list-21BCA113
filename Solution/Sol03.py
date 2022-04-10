#WAS to enter and check it is even number or not.

def evenOdd(n):
    if n%2==0:
        return 1
    else:
        return 0

if __name__=="__main__":

    n=int(input("Enter any No. : "))

    flag = evenOdd(n)
    if flag==1:
        print("{} is even number".format(n))
    else:
        print("{} is odd number".format(n))
    
