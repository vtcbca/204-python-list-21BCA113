#Write a python script to enter two No. & print the sum of it.

def sum(a,b):
    c = a + b
    return c

if __name__=='__main__':
    a=int(input("Enter value for a : "))
    b=int(input("Enter value for b : "))
    d = sum(a,b)
    print("Sum of {} and {} = {}".format(a,b,d))
