#27/07/2026 continue
'''for i in range(1,10):
    if i==6 or i==8:
        continue
    print(i)'''

#without condition
'''for i in range(1,10):
    continue
    print(i)'''

#wap  to skip all the even value within the range

'''for i in range(1,100):
    if i%2==0:
        continue
    print(i)'''
# WAP TO print all the string data present in a list using continue  keyword
'''a=['apple','python','java','c',34,23,'sql','web',2+3j,True]
for i in a:
    if type(i)!=str:
        continue
    print(i)'''
#ASSINGMENT QUESTIONS
#---------------------
#wap tp skip all the palindrome string present in a list
'''l = ["madam", "apple", "level", "python", "radar", "banana"]

for i in l:
    if i == i[::-1]:
        continue
    print(i)'''
#wap to skip all the even values present in list if it is greater than 10

'''l= [2, 5, 12, 15, 18, 7, 20, 9, 14]

for i in l:
    if i % 2 == 0 and i > 10:
        continue
    print(i)'''
#wap to skip all the integers present in odd index

'''l = [2, 3, 4, 5, 6, 7, 'a', 'b']

for i in range(len(l)):
    if i % 2 != 0 and type(l[i]) == int:
        continue
    print(l[i])'''



#(NESTED FOR LOOP)
'''for i in range(2,5):
    for j in range(2,5):
        print(i,j)'''
 

'''for i in range(2,10,2):
    for j in range(2,5):
        print(i+j)'''

#wap to print each and every character present in a string data inside the list

'''l=['apple','banana','grapes','jackfruit']
for i in l:
     for j in i:
         print(j)
     print()'''

#print only vowels in the list

'''l=['apple','banana','grapes','jackfruit']
for i in l:
    for j in i:
        if j in 'AEIOUaeiou':
            print(j)
    print()'''

#print length without USING len function

'''l=['java','python','sql','web','apti']
new=[]
for i in l:
    count=0
    for j in i:
        count=count+1
    new.append(count)
print(new)'''

#wap to print l[100,300,250,500] and the output will be[1050,850,900,650]

'''l = [100, 300, 250, 500]
out=[]
for i in l:
    total=0
    for j in i:
        total =total+j
    out.append(total-i)
print(out)'''


# wap to print l[10,20,40,60] and the output will be [120,110,90,70]




#wap tp sort the list      o/p  [2,3,5,6,7,8]

'''l=[3,2,8,6,5,7]
list2=[]
for i in range(0,len(l)):
    for j in range(len(l)-1):
        if l[j] >l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l[-2])'''

#[6,2,9,7,4,3]

# wap ['i','love','biriyani']   print # o/p={'i':1,'love':4,'biryani':8}

'''l=['i','love','biriyani'] 
new={}
for i in l:
    count=0
    for j in i:
        count=count+1
        
    new[i]=count

print(new)'''

#wap to get following output
#inp='abacbac'
#out='a3b2c2'
'''inp='abacbac'
out=''
for i in inp:#'a'
    if i not in out:
        count=0
        for j in inp:
            if j ==i:
                count=count+1
        out=out+i+str(count)
            
print(out)'''
# l=[1,2,3,4,5] o/p [2,3,4,5,1] ,[3,4,5,1,2]  r=2(for first 2 values)

l = [1, 2, 3, 4, 5]
r = 2

for i in range(r):
    for j in range(len(l) - 1):
        l[j], l[j + 1] = l[j + 1], l[j]   # 
    print(l)








        
