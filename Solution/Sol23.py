"""
WAS to create list using UDF createList(). Count and Print even and odd number in the list using UDF evenOdd().
"""



def evenOdd(l):
    e = []  # List for Even Numbers
    o = []  # List for Odd Numbers
    c = 0  # Flag Value
    d = 0  # Flag Value
    for i in l:
        if i % 2 == 0:
            c += 1
            e.append(i)
        else:
            d += 1
            o.append(i)
    return {'E': e, 'O': o, 'Ec': c, 'Oc': d}


def createList(a):
    l = []
    for i in range(a):
        l.append(int(input("Enter any Integer {} : ".format(i + 1))))
    return l


if __name__ == '__main__':
    a = int(input("Enter List Size : "))
    a = createList(a)
    b = evenOdd(a)
    print("There are total {} even No. in list : ".format(b['Ec'], b['E']), end='')
    for i in b['E']:
        print(i, end=' ')
    print('')
    print("There are total {} odd No. in list : ".format(b['Oc'], b['O']), end='')
    for i in b['O']:
        print(i, end=' ')
