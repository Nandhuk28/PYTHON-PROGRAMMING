#wap to print even or odd
'''check=lambda num:num%2==0
print(check(4))


#wap to print spr of the num
sqr=lambda num:num**2
print(sqr(4))


#WAP TO CHECK whether  first number greater than second  number if it id greater print easy else  hard

sam=lambda num1,num2:'easy'  if num1>num2 else 'hard'
print(sam(5,7))'''


#wap to print square of integer  if it is even else print cube of integer
'''num1= lambda num: num**2 if num%2==0 else num**3
print(num1(5))'''

#wap to print same if str is palindrome else print not same
'''palindrome= lambda word: 'same' if word == word[: : -1]  else 'not same'
print(palindrome('eye'))'''


#wap to find sum of minimum 3 number and maximum 5 number
'''add=lambda a,b,c,d=0,e=0:a+b+c+d+e# default arguments
print(add(10,20,30,5,10))'''

#wap to print vowels if character is vowels else print it is consonent

'''vowels = lambda word: [ch for ch in word if ch in 'AEIOUaeiou']
print(vowels('occurance'))'''

#wap to print long if length of the str is greater than  5 else print short

'''length=lambda string : 'long' if len(string)>5 else 'short'
print(length('table paint '))
'''

#wap to print yes if no is divisble by 3 else print no
'''div= lambda num: 'yes' if num%3==0 else 'no'
print(div(30))'''
#wap to print pass if marks is greater than 35 else print fail
'''mark= lambda num: 'pass'  if num>35  else 'fail'
print(mark(56))'''

#map function

'''l=[8,3,4,1,5,2]
sqr=lambda num: num**2
var=map(sqr,l)
print(list(var))'''#here typecasting because in map its normallay return  address of value after typecasting its return values

#wap to print length of each and every word present in a list
'''l=['nandhini','nathiya','karunagaran','geetha']
leng= lambda count:len(l)
var=map(leng,l)
print(list(l))'''
#wap to get following output a ='good morning '
#o/p={'good':4,'morning':7} in note

#wap to get factorial of all the values present in a colllection

'''l=[3,2,4,1,5,7]
def factorial(n):
    if n==0 or n ==1 :
        return 1
    return n*factorial(n-1)
var=map(factorial,l)
print(list(var))'''

#extract first letter of each word in a list using map
'''l=['book','table','pen','phone']

ext= lambda word: word[0]
var=map(ext,l)
print(list(var))'''
#map function
#convert all the string in a  list to uppercase
'''l=['apple','banana','mango']
upper= lambda word: word.upper()
var=map(upper,l)
print(list(var))'''
#find out each and every type data in list
'''l=['dress',5,3.4,1+3j]
data= lambda word: type(word)
var=map(data,l)
print(list(var))'''



#filter function
'''l=[3,2,4,1,5,7]
even=lambda num:num%2==0
var=filter(even,l)
print(list(var))
'''

#extract palindrome  string from list
'''l=['apple','level','python','eye','racecar']
palin= lambda word: word == word[: : -1] 
var=filter(palin,l)
print(list(var))'''


#extract all the string data from list

'''l=[8,3.2,'1+2j',7,9,'a','b']
string=lambda word:type(word)==str
var=filter(string,l)
print(list(var))'''

#extract muliply of three from list
'''l=[3,6,9,10,45,30]

num=lambda n:n%3==0
var=filter(num,l)
print(list(var))
'''


#wap to yield all string present in list whose length is greater than 7

'''def length():
    l=['polymorphism','encapsulatio','function','string']
    for i in l:
        if len(i)>7:
            yield i

print(list(length()))'''
#wap  to yield all palindrome strings starts with vowel in a list

def palin():
    l=['eye','racecar','wow','level']
    for i in l:
        if  i[0]  in 'AEIOUaeiou' and i==i[: :-1] :
            yield i

print(list(palin()))

#prime number  # filter function

l=[3,7,9,11,8,4,13,7,19]
count=0
for i in l:
    for i in range(1,i+1):
        
        if  i


