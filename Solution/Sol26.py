"""
Create a list of 5 value with filename and extension. Replace extension with".c" with ".py" and print new list.
   filenames = ["program.c", "stdio.c", "sample.c", "a.py", "math.py", "hpp.py"]
   Output: filenames = ["program.py", "stdio.py", "sample.py", "a.py", "math.py", "hpp.py"]
"""

a = []
b = []
for i in range(5):
    s = input('Enter the filename with extension : ')
    a.append(s)
print('Filename you entered :', a)
r = input('Enter Current Extension : ')
n = input('Enter New Extension : ')
for i in a:
    a = i.replace(r, n)
    b.append(a)
print('Filenames with new Extension : ', b)
