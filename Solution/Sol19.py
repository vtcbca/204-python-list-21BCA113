'''
WAP to create UDF which create 2 list Student and Address which contain student name and respected address of student.

Create new UDF which print student name with appropriate student address.
'''

std = ["OM","Sai","Ram"]
add = ["Bardoli","Surat","Navsari"]

def prnt():
    for i in range(3):
        print("{0} Lives in {1}".format(std[i],add[i]))
prnt()
