# wap to print sum of factorial of a num by using recursion
 
'''def fact(n):
    if n==0 or n==1:
        return 1
    return n+fact(n-1)
print(fact(5))'''

# wap to print product of factorial of a num by using recursion

'''def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)
print(fact(5))'''

#wap to count the number of uppercase character present in a string

'''def v_count(s,c=0,i=0):
    if i >= len(s):
        return c
    if s[i] in 'AEIOUaeiuo':
        c=c+1
    return v_count(s,c,i+1)
print(v_count('education'))'''


#wap to count the number of uppercase character present in a string
'''def v_count(s,c=0,i=0):
    if i >= len(s):
        return c
    if 'A'<= s[i] <= 'Z':
        c=c+1
    return v_count(s,c,i+1)
print(v_count('EDuCATION'))'''

# wap to reverse the number using recursion

'''def reverse(n,rev=0):
    if n==0:
        return rev
    while n!=0:
        ld=n%10
        rev=(rev*10)+ld
        n=n//10
    return reverse(n,rev)
print(reverse(int(input('enter a number'))))'''


#2 methode
'''def reverse(num,rev=0):
    if num==0:
        return rev
    ld=num%10
    rev=(rev*10+ld)
    return reverse(num//10,rev)
print(reverse(123))'''



#Assignments question   5/08/2026

#wap to extract all the integer present in a list

def exc(li, new=[], i=0):
    if i >= len(li):
        return new

    if type(li[i]) == int:
        new.append(li[i])

    return exc(li, new, i + 1)

print(exc([23, 67, 87, 'value', 3.6, 45, 'abc']))
            

#wap to reverse the string using recursion
def reverse(s, rev="", i=0):
    if i == len(s):
        return rev

    rev = s[i] + rev
    return reverse(s, rev, i + 1)

print(reverse("python"))
    

#wap get all the even number in a list
def even_num(l):
    new = []

    for i in l:
        if i % 2 == 0:
            new.append(i)

    return new

print(even_num([12, 7, 8, 15, 20, 33, 40]))
# wap to get the count of palindrome strings in a list
def palindrome_count(l):
    count = 0

    for s in l:
        rev = " "

        for i in s:
            rev = i + rev

        if s == rev:
            count += 1

    return count

l = ["madam", "python", "level", "hello", "radar"
print(palindrome_count(l))# may be slicing
     
