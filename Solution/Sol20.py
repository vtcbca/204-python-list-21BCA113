'''
WAP to create UDF to check string palindrome or not.
'''

inp = input("Enter a String : ")

def pal(a):
    b = a
    b = a[::-1]
    if b != a:
        print(a + " is not Pelindrome String" )
    else:
        print(a + " is Pelindrome String")
pal(inp)
