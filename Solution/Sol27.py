"""
WAS to create list with 5 string and print only even number character of each string using UDF.
"""


def evenchar(a):
    for i in a:
        n = []
        for j in range(len(i)):
            if j % 2 != 0:
                n.append(i[j])
        print('Even characters in " {} " :'.format(i))
        print(n)

if __name__=='__main__':
    a = []
    for i in range(5):
        s = input('Enter String {} : '.format(i+1))
        a.append(s)
    evenchar(a)
