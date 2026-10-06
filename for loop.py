'''l=[1,2,3,'s','k',3.2]
for i in l:
    print(i)
-------------------------------------'''
'''t=('c','python','c','java')
for i in t:
    print(i)
------------------------------------'''

'''s={'a','b',3,4,5,8,8,5}
for i in s:
    print(i)
-------------------------------------'''
'''d={'a':1,'b':2,'c':3}
for i in d:
    print(i,d[i])
-------------------------------------'''
'''s='abdul rahaman'
for i in s:
    print(s,'\n')
-------------------------------------'''
'''for i in range(1,11,1):
    print(i)
--------------------------------------'''
#wap to check length of coll without using len function
'''collection=[10,20,30,40,50]
count=0
for i in collection:
    count=count+1

print(count)
-----------------------------------------------'''
#wap to extract all the string data present in list
'''li=[1,2,3,'case','madam','java','python',3.1]
new_list=[]

for i in li:
    if type(i)==str:
        new_list.append(i)

print(new_list)
-----------------------------------------------------------------'''
#wap to extract all the even number present in a list data
#[2,6,5,3,9,12,333,45,77,68,92]
'''list=[2,6,5,3,9,12,333,45,77,68,92]
even=[]

for i in list:
    if i%2==0:
        even.append(i)

print(even)
------------------------------------------------------------------------'''
# wap to extract all the  palindrome string present in a list
#p=['level','racecar','eye','python','malayalam','apple','grapes']
#['level','racecar','eye','malayalam']
'''p=['level','racecar','eye','python','malayalam','apple','grapes']
palindrome=[]
for i in p:
    if i==i[: : -1]:
        palindrome.append(i)
print(palindrome)
--------------------------------------------------------------------'''
# wap to extract all the uppercase character present in a string
#s=' hi how are you'
#upper='HHOWEU'
'''s=' Hi HOW arE yoU'
upper=[]
for i in s:
    if 'A' <= i <= 'Z':
        upper.append(i)

print(upper)
--------------------------------------------------------------------'''
# wap to print number from 100 to 1 using for loop

'''for i in range(100,1,-1):
    
    print(i)
--------------------------------------------------------------------------------'''
# wap to extract all the integer present in a list which is is divisible by 3

'''l=[99,66,'kiran',82,74,15,18,36,'apple','a','python']
intlist=[]
for i in l:
    if type(i)==int and i%3==0:
        
        intlist.append(i)
print(intlist)
------------------------------------------------------------------------------'''
#wap to print key and value if keys are string data from dict
'''d={'sid':123,1:3,4:5,'sname':'vasanth','semail':'vasanth@123'}
for i in d:
    if type(i)==str:
        print(i,d[i])

#2nd method

d={'sid':123,1:3,4:5,'sname':'vasanth','semail':'vasanth@123'}
new={}
for i in d:
    if type(i)==str and type(d[i])==int:
        new[i]=d[i]
print(new)

-------------------------------------------------------------------------'''

#wap to get the following o/p
'''d={'a':'a',2:2,4:5,9:3.5,'apple':'apple'}
out={'a':'a',2:2,'apple':'apple'}

#wap to get following o/p
a=['python','is','very','easy']
out=['python':6,'is':2,'very':4,'easy':4]

----------------------------------------------------------------------'''
#wap to get the frequency of a string in dictionary
'''s='hello'
new={}
for i in s:
    if i not in new:
        new[i]=1
    else:
        new[i]=new[i]+1
        
print(new)
----------------------------------------------------------------------'''
#wap to remove duplicate values in list data
'''l=[1,1,2,1,3,3,4,2,4,5,6]
out=[]
for i in l:
    if i not in out:      #if i in l2 and i not in common: 
        out.append(i)

print(out)'''

#wap identify max value from the list data

'''l=[67,32,44,56,9,45,79,34]

maxnum=0
for i in l:
    if i > maxnum:
        maxnum=i

print(maxnum)
----------------------------------------------------------'''
#wap to extract common elements from 2 diiferent list
'''l1=[3,2,5,7,11]
l2=[5,15,11,13,4,7,2]
common=[]
for i in l1:
    if i in l2:
        common.append(i) 

print(common)
--------------------------------------------------------'''
#between range 100 to 1 fizz-->3% , buzz-->5%, fizzbuzz-->3%&5%

'''for i in  range(10,1,-1):
    if i%3==0 and i%5==0:
        print('fizzbuzz')
    elif i%3==0:
        print('fizz')
    elif i%5==0: 
        print('buzz')
    else:
        print(i)
----------------------------------------------------------------'''
        
#wap to get the following output
'''d={'a':'a',2:2,4:5,9:3.5,'apple':'apple'}
#out={'a':'a',2:2,'apple':'apple'}
d2={}
for i in d:
    if i==d[i]:
         d2[i] = d[i]
         
print(d2)'''

#wap to get the following output
'''a={'python','is','very','easy'}
out={}
#out={'python':6,'is':2,'very':4,'easy':4}
for i in a:
    out[i]=len(i)

print(out)'''

#2nd method
'''a={'python','is','very','easy'}
out={}
for i in a:
    if i=='python':
        out[i]='prog'
    elif i=='is':
        out[i]='operator'
    elif i=='very':
        out[i]='word'
    elif i=='easy':
        out[i]='4'
print(out)'''
        
#wap to print vowels present in even index of string data
'''s='education'
for i in range(0,len(s)):
    if i%2==0 and s[i] in 'AEIOUaeiou':
        print(s[i])'''
'''s='education'
for i,j in enumerate(s):
    if i%2==0 and j in 'AEIOUaeiou':
        print(i)'''

'''s='education'
for i,j in enumerate(s):
    print(i, j)'''

#tranfer condition
#1
'''for i in range(2,10):
    if i==3:
        print(i)
    break
#2
for i in range(2,10,2):
    if i==3:
        break
    print(i)

#3
for i in range(2,10):
    if i==3 or i==5:
        print(i)
    break
#4
for i in range(2,10,2):
    if i==4 or  i==6:
        break
    print(i)

#5
for i in range(1,10):
    print(i)
    break
#6
for i in range(1,10):
    break
    print(i)

#7*
for i in range(1,10,2):
    if i==3 or i==5:
        break
    print(i)

#8
for i in range(2,10,2):
    if i==3 or i==2:
        print(i)
    break

#9

for i in range(2,5):
    if i>3:
        print(i)
    break

#10

for i in range(2,10):
    if i>7:
        break
    print(i)

--------------------------------------'''
l=['a','b','c','d',4,3.4,8.3,2+3j,[1,2,3]]


'''for i in l:
    if type(i)!=str:
        break
    print(i)'''

























