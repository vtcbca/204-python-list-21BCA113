# Menu
def men():
    print("_____ Menu _____")
    print("1 For Frequency Of Characters ")
    print("2 For Frequency Of Words")
    print("3 For Unique Characters Of String")
    print("4 For Words Length Greater Than N")

def fows(st):  # Frequency of Words In String
    st = st.split()
    C = []
    B = []
    A = []
    for i in st:            #For Loop To Separately Store Words
        C.append(i)
    for i in C:             #For Loop To Count Frequency and Append Values
        flag = 0
        for j in C:
            if i == j:
                flag = flag + 1
        if i not in A:
            B.append(flag)
            A.append(i)
    for i in range(len(B)):
        print(A[i], B[i], sep=' ---> ')


def focs(st):  # Frequency of Character In String
    st = st.split()
    C = []
    B = []
    A = []
    for i in st:        #for loop to separately Store Characters
        for j in i:
            C.append(j)
    for i in C:         #For Loop To Count Frequency and Append Values
        flag = 0
        for j in C:
            if i == j:
                flag = flag + 1
        if i not in A:
            B.append(flag)
            A.append(i)
    for i in range(len(B)):
        print(A[i], B[i], sep=' ---> ')

def ucis(st):
    st = st.split()
    A = []
    B = []
    C = []
    for i in st:        #for loop to separately Store Characters
        for j in i:
            C.append(j)
    for i in C:         #For Loop To Count Frequency and Append Values
        flag = 0
        for j in C:
            if i == j:
                flag = flag + 1
        if i not in A:
            B.append(flag)
            A.append(i)
    for i in A:
        print(i, end=', ')

def wlgti(st):
    inp = int(input("Enter The Length : "))
    st = st.split()
    for i in st:
        if len(i)>inp:
            print(i)

if __name__ == "__main__":      #If The File Fun Directly Functions Will Work Or Else you Can Import the File As Library To Use Functions.
    # String Input
    Str = []
    Str = input("Enter The String : ")

    men()           #print Menu using Function

    A = int(input("Enter Your Choice : "))  #Input of Choice

    if A == 1:
        focs(Str)       #Frequency Of Characters Function
    elif A == 2:
        fows(Str)       #Frequency Of Words Function
    elif A == 3:
        ucis(Str)       #Unique Character From String Function
    elif A == 4:
        wlgti(Str)      #Words Greater Than User Defined Value Function
    else:
        print("Enter Correct Choice")

