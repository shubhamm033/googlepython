import re

def Find(pat,text):
    match=re.search(pat,text)
    if match:
        print match.group()
    else:
        print 'not found'

#Find(r':\w\w\w','blah :scat blah blah   lelele   ledddddd')
###### if looking for a particular type of character
####Find(r'[\w.]+@[\w.]+','blah shubham.m0333@gmail.com ddddlll')
m=re.findall(r'[\w.]+@[\w.]+','blah shubham.m0333@gmail.com ddddlll foo@gmail')


print m