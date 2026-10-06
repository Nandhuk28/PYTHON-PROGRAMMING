#inheritance
'''class A:
    a=10
    b=20


class B(A):
    c=40
    d=45


print(A.a,A.b)
print(B.a,B.b,B.c,B.d)'''

#instagram class using
'''class instagram:
    def messenger(self):
        print('sending messenger')


class instagram1(instagram):
    def reels(self):
        print('upload reels')

    def threads(self):
        print('upload threads')


u1=instagram1()
u1.reels()
u1.threads()
u1.messenger()'''

#constructor chaining# super chaining
'''class basic_details:
    def __init__(self,sname,sphno,smail):
        self.sname=sname
        self.sphno=sphno
        self.smail=smail
    def display(self):
        print(self.sname,self.sphno,self.smail)

class education(basic_details):
    def __init__(self,sname,sphno,smail,per10,per12,degreeper):
        super().__init__(sname,sphno,smail)#constructor chaining
        self.per10=per10
        self.per12=per12
        self.degreeper=degreeper

    def edu_display(self):
        super().display#methode chaining
        print(self.per10,self.per12,self.degreeper)
s1=education('aryan',894928489298,'arya123',89,73,37)
s1.display()
s1.edu_display()'''


#multi level inheritence      methode&constructor chianing

'''class basic_details:
    def __init__(self,sname,sphno,smail):
        self.sname=sname
        self.sphno=sphno
        self.smail=smail
    def b_display(self):
        print(self.sname,self.sphno,self.smail)

class education(basic_details):
    def __init__(self,sname,sphno,smail,per10,per12,dper):
        super().__init__(sname,sphno,smail)
        self.per10=per10
        self.per12=per12
        self.dper=dper
    def edu_display(self):
        print(self.per10,self.per12,self.dper)
class resume(education):
    def __init__(self,sname,sphno,smail,per10,per12,dper,yexp,company_name):
        super().__init__(sname,sphno,smail,per10,per12,dper)
        self.yexp=yexp
        self.company_name=company_name

    def R_display(self):
        print(self.yexp,self.company_name)

R1=resume('nandhu',8938929478248,'nan@122',78,98,87,0,'unknown')
R1.b_display()
R1.edu_display()
R1.R_display()'''

#MULTIPLE INHERITANCE

'''class basic_details:
    def __init__(self, sname, smail):
        self.sname = sname
        self.smail = smail

    def b_display(self):
        print(self.sname, self.smail)


class education:
    def __init__(self, rank, per):
        self.rank = rank
        self.per = per

    def edu_display(self):
        print(self.rank, self.per)


class resume(basic_details, education):
    def __init__(self, sname, smail, rank, per, qualification, exp):
        basic_details.__init__(self, sname, smail)
        education.__init__(self, rank, per)

        self.qualification = qualification
        self.exp = exp

    def r_display(self):
        print(self.qualification, self.exp)


r1 = resume('nandhu', 'nan@123', 1, 78, 'MCA', 1)

r1.b_display()
r1.edu_display()
r1.r_display()'''
        
#heirarichal inherit

'''class features:
    def chat(self):
        print('chat is enabled')
    def add_story(self):
        print('u can add story')

class whatsapp(features):
    def payment(self):
        print('payment is enabled')

class instagram(features):
    def threads(self):
        print('threads uploaded')
        
w1=whatsapp()
w1.chat()

w1.payment()
w1.add_story()

I1= instagram()
I1.chat()
I1.threads()
I1.add_story()'''

#hybrid inherit

class addition:
    @staticmethod
    def add(a,b):
        print(a+b)
class  subtraction:
    @staticmethod
    def sub(a,b):
        print(a-b)

class multiplication(addition,subtraction):
    @staticmethod
    def mul(a,b):
        print(a*b)

class calculator(multiplication):
    @staticmethod
    def div(a,b):
        print(a/b)

c1=calculator()
c1.add(10,20)
c1.sub(10,20)
c1.mul(10,20)
c1.div(10,20)
