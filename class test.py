# 1 wap  to check whether the last value of a num is even no or not
'''s=[1,2,3,4,5]
if type(s[4])==int:
    print('its is integer')
else:
    print('its not an integer')
    #divisible methods are available'''

#2 method
num=eval(input())
if num[-1]%2==0:
        print('its an even number')
else:
        print('odd number')




     
#2..wap  to check whether the string is pakindrome and having length  grether than 10 or not
'''s=input('enter a character')
if s==s[ : :-1] and  len(s)<10:
    
    print('its a palindrome')

else:
    print(f'{s} it is not a palindrome its is less than 10 char')

-------------------------------------------------------------------------------------------------'''

# 3... wap to check whether list is palindrome or not if it is palindrome print 1st value and last value of list else print between values
'''li = ['racecar', 'nan', 'dad', 'madam']

if li == li[::-1]:
    print(li[0], li[-1], 'it is palindrome')
else:
    print(li[1], li[2], 'it is not a palindrome')

-------------------------------------------------------------------------------------------------'''
    
# 4 ..wap to check last value of list is string and its starts with  vowels or not
'''li=['a','b','c','d']
if type(li[3])==str  and li[0] in 'AEIOUaeiou':
    print('its start with vowles ')
else:
    print('not start with vowels')
--------------------------------------------------------------------------------------------------'''

# 5.. wap to check whether num is even and its is divisible by 5 or not

'''num=int(input('enter a number'))
if num%2==0 and num%5==0 :

        print('its is even and divisible by 5')
else:
        print('not divisble by 5')

---------------------------------------------------------------------------------------------------'''
#.6.. wap to check the data is mutable or immutable

'''data = eval(input('Enter a value: ')) 
if type(data) in [list, dict, set]: 
    print('mutable') 
else: 
    print('immutable')

---------------------------------------------------------------------------------------------------'''
#.7..wap  to check length of the list is odd or even if it is even append new value if it is odd delete last value from list
'''li=[1,2,3,4,5]
if len(li)%2==0:
    li.append(6)
    print(li)
elif len(li)%2==1 :
    li.remove(5)
    print(li)
--------------------------------------------------------------------------------------------------'''

# 8..wap to print hi if num is divisible by 3 and print hello if it is divisble by 7 and print hihello if it is divisble by both 3 and 7
'''num=int(input('enter a number'))
if num%3==0 and num%7==0:
    print('hihello')
elif num%3==0:
    print('hi')
elif num%7==0:
    print('hello')

--------------------------------------------------------------------------------------------------'''
# 9..identify whether sales person got profit or loss or none
'''product ='lenovo laptop'
selling_price ='56000'
cost_price='33000'

if cost_price<selling_price:
    print('profit')
elif  cost_price >selling_price:
    print('loss')
else:
    print('none')

--------------------------------------------------------------------------------------------------'''


#.10..sal=int(input('enter a value'))
#check sal greater than  50000 and that into high sal list
# if it is in between 20000 to 50000 add for mid sal list
# if it is less than 20000 add to low sal list


'''sal = int(input("Enter salary: "))

high_sal = []
mid_sal = []
low_sal = []

if sal > 50000:
    high_sal.append(sal)
elif sal > 2000 and sal < 5000:
    mid_sal.append(sal)
elif sal < 2000:
    low_sal.append(sal)

print("High salary:", high_sal)
print("Mid salary:", mid_sal)
print("Low salary:", low_sal)
------------------------------------------------------------------------------------------------'''




# 13... wap to print the count  vowels  present in a string
'''st=input()
count=0
i=0
while i<len(st):
        if st[i]in'AEIOUaeiou':
                count+=1
        i+=1
print(count)'''

# 11..wap to print * in empty space  
'''st=input("enter the string:")
i=0
result=''
while i<len(st):
        if st[i] ==' ':
                result=result+"*"
        else:
                result=result+st[i]
        i+=1
print(result)
------------------------------------------------------------------------------------------------'''
# 12..wap to count the occurannce of a particular character in a string
'''st=input()
st2=input()
i=0
count=0
while i<len(st):
        if st2==st[i]:
                count+=1
        i+=1
print(count)'''



                        
        
