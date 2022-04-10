#WAS to enter any number and print approprite days name
def days(a):
    if a==1:
       return "Sunday"
    elif a==2:
        return "Monday"
    elif a==3 :
        return "Tuesday"
    elif a==4:
        return "Wednesday"
    elif a==5:
        return "Thursday"
    elif a==6:
        return "Friday"
    elif a==7:
        return "Saturday"
    else:
        return "Invalid Input"

if __name__=="__main__":
    a = int(input("Enter any No. between 1 to 7 : "))
    a = days(a)
    print(a)

    
