__author__ = 'Ayla'

#1
def python(s):
    len(s)
    if len(s) <= 5:
        print(s)
    else:
     if len(s) > 5:
        return None




s="Python"
print(python(s[]))

#2
def python(s):
    a=''
    for i in reversed(range(len(s))):
        a=a+s[i]
        print(s[i])
    print(a)

(python('python'))


