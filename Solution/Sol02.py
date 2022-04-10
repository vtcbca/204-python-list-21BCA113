#WAS to enter kilometer and converted it into meter.

def kmtm(km):
    ans = km*1000
    return ans

if __name__=='__main__':
    km = float(input("Enter a value of kilometer : "))
    ans = kmtm(km)
    print("{} Km = {} meter".format(km, ans))