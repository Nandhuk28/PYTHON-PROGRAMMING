l=[1,8,3,7,3.4,'a','d']

temp=type(l[0])
for i in l:
    if type(i)!=temp:
        print('hetrogenus')
        break
else:
    print('hemogenus')
#***infinite loop

import random
num =random.randint(1,20)
entries=10
i=1
while i<=entries:
    choice=int(input('enter your num'))
    if num==choice:
        print('num is matched')
        break
    elif num>choice:
        print('enter larger number')
    elif  num<choice:
        print('enter lower number')

    i=i+1

    
