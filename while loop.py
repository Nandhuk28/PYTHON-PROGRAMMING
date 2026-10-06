#wap a prog mulitiplication of n natural number 
                    #[or]
# impt question ----- wap to print factorial of a num
'''i=1
n=int(input('enter a n value'))
mul=1   
while i<=3:
    mul=mul*i
    i=i+1

print(mul)

-----------------------------------------------------------------------'''

# wap to get sum even number beteween range 0 to 20
'''i = 0
sum = 0

while i <= 20:
    sum = sum + i
    i = i + 2

print(sum)
----------------------------------------------------------------------'''

# wap to get the sum odd number between range 1 to 30
'''i=1
sum=0

while i <= 30:
    sum=sum +i
    i = i + 2

print(sum)
--------------------------------------------------------------------------'''
# wap to print num from 20 to 1

'''i=20

while 1<=i :
    print(i)
    i=i-1
print(i)

---------------------------------------------------------------------------'''
# wap prg to print all the vowels preseent inside string
'''s=input('enter your string')
i=0
while i <len(s):
    if s[i] in  'AEIOUaeiou':
        print(s[i])
        i=i+1

-----------------------------------------------------------------------------'''
#wap a prog reverse the string
'''s='nandhini'
i=7
while 0<=i:
    print(s[i])
    i=i-1
print(i)'''

'''-------------------------------------------------------------------------------'''
'''s= input('enter your string ')
i=0
rev=' '
while i <len(s):
    rev=s[i]+rev
    i=i+1

print(rev)
---------------------------------------------------------------------------------'''

#important questions
#===================
#wap to product of  all the digits present inside the num
'''num=int(input('enter your number'))
product=1
while num!=0:
    ld=num%10
    product=product*ld
    num=num//10
    print(product)
------------------------------------------------------------------------'''
#wap to reverse the number without using typecasting
'''num=int(input('enter your number'))#123
rev=0
while num!=0:
    ld=num%10
    rev=(rev*10)+ld
    num=num//10
    print(rev)
-------------------------------------------------------------------------'''
#wap to check whether num is arm -strong num or not
'''num=153
num_length=len(str(num))#3
sum=0
temp=num
while num!=0:
     ld=num%10
     sum=sum+(ld**num_length)
     num=num//10
if temp==sum:
    print('num is arm strong')
else:
    print('not an arm strong')
-----------------------------------------------------------------------------------'''
#2nd method
'''num=1634
num_length=len(str(num))
sum=0
temp=num
while num!=0:
     ld=num%10
     sum=sum+(ld**num_length)
     num=num//10
if temp==sum:
    print('num is arm strong')
else:
    print('not an arm strong')
---------------------------------------------------------------------------------------------'''
#wap  to get count of digits present in a number using while loop#5378347
'''num=5378347
count=0
while num>0:
     num=num//10
     count=count+1

print('count=',count)
-----------------------------------------------------------------------------------------'''
 #wap to check num is prefect num or not
'''num = int(input("Enter a number: "))
i = 1
sum = 0
while i < num:
    if num % i == 0:
        sum = sum + i
    i = i + 1
if sum == num:
    print("Perfect number")
else:
    print("Not a perfect number")
---------------------------------------------------------------------------------------------'''
# wap to get sum of sqr of all the digits present in a num#325

'''num=325
sum=0
num_length=len(str(num))

while num!=0:
     ld=num%10
     sum=sum+(ld*ld)
     num=num//10
print(sum)
-----------------------------------------------------------------------------------------------'''

     






















