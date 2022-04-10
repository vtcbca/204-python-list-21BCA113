"""
Create a list using UDF by appending points of cricket team after completing their qualifying round of 5 teams.
Print the runner's team point. Note: There is a chance that 2 or more teams gets a same point. Also, there is no
possibility that each team has same points.
    For example :
    case 1: point=[10,8,14,6,12]
    Output : 12
    case 2: Point=[10,8,14,14,12]
    output:  12
    case 3: Point=[10,8,12,14,12]
    output:  12,12
"""


def team(l):
    c = 0
    l1 = []
    l2 = []
    while l:
        i = l[0]
        for j in l:
            if i > j:
                i = j
        l1.append(i)
        l.remove(i)
    for i in l1:
        if i < l1[-1]:
            c = i
    for i in l1:
        if i == c:
            l2.append(i)
    print("Runnerup : ", l2)


if __name__ == "__main__":
    l = []
    for i in range(5):
        a = int(input('Enter the team score : '))
        l.append(a)
    team(l)
