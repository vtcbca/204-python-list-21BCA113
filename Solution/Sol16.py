'''
Write a script to enter any word and check it is palindrome or not.
'''

st = input("Enter any string : ")
rst = "".join(reversed(st))
if st == rst:
    print("{} is palindrome".format(st))
else:
    print("{} is not palindrome.".format(st))
