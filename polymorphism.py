#before overloading
'''def add(a,b):
    print(a+b)

def add(a,b,c):
    print(a+b+c)

add(10,20)'''

#after overloading
'''def add(a,b):
    print(a+b)
temp=add#monkey patching
def add(a,b,c):
    print(a+b+c)

temp(10,20)
add(10,20,30)
 
#magic methods
dir(str)
dir(int)'''

#operator overloading

class A:
    def __init__(self,a):
        self.a=a

    def __add__(self,other):
        return self.a+other.a

    def __sub__(self,other):
        return self.a-other.a

    def __mul__(self,other):
        return self.a*other.a

    def __floordiv__(self,other):
        return self.a//other.a
    


oa=A(10)
ob=A(20)
print(oa+ob)# + is used to call __add__ magic method
print(oa-ob)# - is used to call __sub__ magic method
print(oa*ob)
print(oa//ob)
