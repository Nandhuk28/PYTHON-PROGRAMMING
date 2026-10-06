#30/7
#wap to perform addition of 2 num using
'''def add():
    a=10
    b=20
    print(a+b)
add()'''
#wap to count the number of vowels present in a string
'''def count():
    s='usinglaptop'
    sum=0
    for i in s:
        if i in 'AEIOUaeiou':
            sum=sum+1
    print(sum)
count()
#wap to remove duplicate character in a string
def remove():
    s = "programming"
    result = ""

    for ch in s:
        if ch not in result:
            result = result + ch
    print(result)

remove()'''
#wap to extract only even integers present in a list 
'''def even_numbers():
    l = [10, 15, 20, 25, 30, 35, 40, 45]
    even = []

    for i in l:
        if i % 2 == 0:
            even.append(i)

    print(even)

even_numbers()'''

#31/7

#wap to move zeros at last in a list

'''def move(l,zero,non_zero):
    for i in l:
        if i==0:
            zero.append(i)
        else:
            non_zero.append(i)
    print(non_zero+zero)
move([2,0,3,4,5,60,6,9,0],[],[])'''
#wap to check whether the num is spy number or not
#@function without arguments and without return value
'''def spy():
    n = int(input("Enter a number: "))
    temp = n
    s = 0
    p = 1

    while temp > 0:
        digit = temp % 10
        s = s + digit
        p = p * digit
        temp = temp // 10

    if s == p:
        print(n, "is a Spy Number")
    else:
        print(n, "is Not a Spy Number")

spy() '''   

#function with arguments (without return)
'''def spy(n):
    temp = n
    s = 0
    p = 1

    while temp > 0:
        digit = temp % 10
        s = s + digit
        p = p * digit
        temp = temp // 10

    if s == p:
        print(n, "is a Spy Number")
    else:
        print(n, "is Not a Spy Number")

num = int(input("Enter a number: "))
spy(num)'''

#wap to count the even add values   and odd present   in a list of integers
#l=[21,36,83,93,93,32,46,48](with arg without return)
def count(l):
    odd=0
    even=0
    for i in l:
        if i%2==0:
            even=even+1
        else:
            odd=odd+1
    print('even=',even)
    print('odd=',odd)

count([21,36,83,93,93,32,46,48,90,44,56,78])
            
    

#wap to get the following output
#s='programming'
#output='poain'
'''def remove():
    s = "programming"
    result = ""

    for ch in s:
        if s.count(i)==1:
            result = result + ch
    print(result)

remove()'''


#wap to return number digits present in a string#3
'''def vowels():
    s='Qspiders@143@gamil.com'
    count=0
    
    for i in s:
        if  i in  '0123456789':
            count=count+1
    return count
    

print(vowels())'''
        

    
#wap to get the sum of digits present in a string#8
'''def vowels():
    s='Qspiders@143@gamil.com'
    sum=0

    for i in s:
        if i>='0' and i <='9':
            sum=sum+int(i)
    return sum
print(vowels())'''


#wap to return number vowels present in a string#5

'''def vowels():
    s='Qspiders@143@gamil.com'
    count=0
    
    for i in s:
        if  i in  'AEIOUaeiou':
            count=count+1
    return count
    

print(vowels())'''
# wap to return the index  value of max num in a list  #enumrate function using

'''def maxi():
    l = [12, 73, 83, 93, 8, 82]
    index = 0

    for i in range(1, len(l)):
        if l[i] > l[index]:
            index = i

    print("Maximum value =", l[index])
    print("Index =", index)

maxi()
#USING enumrate

def maxi():
    l = [12, 73, 83, 93, 8, 82]

    index = 0
    max_value = l[0]

    for i, j in enumerate(l):
        if j > max_value:
            max_value = j
            index = i

    print("Maximum =", max_value)
    print("Index =", index)

maxi()'''

#with arg & with return         3/08/2026
# 29/07/2026



#types of arguments
#-------------------
# keyword ARGUMENTS ( where u want declared keyword ,values)
'''def std_details(sid,sname,sloc,sphno):
    print(f'student id is:{sid},sname is:{sname},sloc is{sloc},sphno is:{sphno}')
std_details(sname='kiran',sid='234',sphno='8730826278',sloc='velacherry')'''


# positional arguments(want decalared 4 variables 4 values)

'''def std_details(sid,sname,sloc,sphno):
    print(f'student id is:{sid},sname is:{sname},sloc is{sloc},sphno is:{sphno}')
std_details(234,'kiran','chennai',728942967228)'''


# default arguments( want to declared defaultly giving values to variable)

'''def std_details(sid,sname,sphno,sloc='vridhachalam',):
    print(f'student id is:{sid},sname is:{sname},sloc is{sloc},sphno is:{sphno}')
std_details(234,'kiran',728942967228)'''

#assigments qs on before  4 questions with arg with return(with return with arg)
##-----------------------------------------------------------
#wap to return number digits present in a string#3
'''def vowels(s):
    
    count=0
    
    for i in s:
        if  i in  '0123456789':
            count=count+1
    return count
    

print(vowels('Qspiders@143@gamil.com'))'''

#wap to return number vowels present in a string#5
'''def vowels(s):

    count=0
    
    for i in s:
        if  i in  'AEIOUaeiou':
            count=count+1
    return count
    

print(vowels('Qspiders@143@gamil.com'))'''

#wap to get the sum of digits present in a string#8
'''def vowels(s):
    
    sum=0

    for i in s:
        if i>='0' and i <='9':
            sum=sum+int(i)
    return sum
    

print(vowels('Qspiders@143@gamil.com'))'''

# wap to return the index  value of max num in a list  #enumrate function using
'''def maxi(l):
    

    index = 0
    max_value = l[0]

    for i, j in enumerate(l):
        if j > max_value:
            max_value = j
            index = i

    print("Maximum =", max_value)
    print("Index =", index)

maxi([12, 73, 83, 93, 8, 82])'''


#calculator program
'''def add(a, b):
    print(a + b)

def subract(a, b):
    print(a - b)

def multiply(a, b):
    print(a * b)

def divid(a, b):
    print(a / b)     # Use / for division

def inp():
    a = int(input("Enter 1st value: "))
    b = int(input("Enter 2nd value: "))
    return a, b

print(
Enter 1 for Add
Enter 2 for Subtract
Enter 3 for Multiply
Enter 4 for Divide
Enter 5 to Stop
)

while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        x, y = inp()
        add(x, y)

    elif choice == 2:
        x, y = inp()
        subract(x, y)

    elif choice == 3:
        x, y = inp()
        multiply(x, y)

    elif choice == 4:
        x, y = inp()
        divid(x, y)

    elif choice == 5:
        print("Program Stopped")
        break

    else:
        print("Invalid Choice")'''
