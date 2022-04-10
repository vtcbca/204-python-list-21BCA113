def unique(l):
    a = []
    for i in l:
        if i not in a:
            a.append(i)
    return a


def duplicate(a):
    l = []
    for i in range(a):
        l.append(int(input('Enter any integer {} : '.format(i+1))))
    a = unique(l)
    return a


if __name__ == '__main__':
    a = int(input("Enter List Size : "))
    a = duplicate(a)
    print('Unique Values Of Your List : ', a)
