"""
WAS to enter any number and print the prime number between 1 to n number using UDF primeNo().
"""
def primeNo(n):
    for i in range(1,n+1):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i)

if __name__=='__main__':
    n = int(input('Enter the value of N : '))
    print('Following are the prime No. between 1 to', n)
    primeNo(n)

