'''
WAS to create 2 udf input() to take input string and call strSymmetric() by passing inputted string.
'''

def strSym(st):
    a = st
    l = len(st) // 2
    if st[:l] == st[l:]:
        print(a + " is Symmetric ")
    else:
        print(a + " is Not Symmetric")

def inp():
    return input("Enter String : ")

if __name__ == '__main__':
    inp = inp()
    strSym(inp)
