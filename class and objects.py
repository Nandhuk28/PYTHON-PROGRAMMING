#constructor
'''class institude:
    Iname='jspider'
    Iloc='velacherry'
    Imanager='shubham'


    def __init__(self,sid,sname,sphno):
        self.sid=sid
        self.sname=sname
        self.sphno=sphno
        print(self)


s1=institude(106,'sakthi',6772787891)
s2=institude(107,'nandhu',7384784969)


print(s1.sid,s1.sname,s1.sphno)
print(s2.sid,s2.sname,s2.sphno)'''


#types of methods
#obj methods
'''class institude:
    Iname='jspider'
    Iloc='velacherry'
    Imanager='shubham'


    def __init__(self,sid,sname,sphno):
        self.sid=sid
        self.sname=sname
        self.sphno=sphno
        
    def display(self):
        print(self.sid,self.sname,self.sphno)

    #modify
    def modify_sname(self,new_name):
        self.sname=new_name


s1=institude(106,'sakthi',6772787891)
s2=institude(107,'nandhu',7384784969)
s3=institude(108,'tamil',78348048411)
s4=institude(109,'akash',7858778878)
print(s1.sid,s1.sname,s1.sphno)
print(s2.sid,s2.sname,s2.sphno)
print(s3.sid,s3.sname,s3.sphno)
print(s4.sid,s4.sname,s4.sphno)

ob=[s1,s2,s3,s4]
for i in ob:
    i.display()

s1.display()
s1.modify_sname('surya')
s1.display()'''

#atm assingments

'''class ATM:
    bname = 'HDFC'
    bloc = 'Vel'
    bifsc = 'HDFC000'

    def __init__(self, cid, cname, cpin, cbal):
        self.cid = cid
        self.cname = cname
        self.cpin = cpin
        self.cbal = cbal

    def check_balance(self):
        upin = int(input('Enter your pin: '))

        if self.cpin == upin:
            print(f'Your current balance is: {self.cbal}')
        else:
            print('Invalid pin')

    def deposit(self):
        amount = int(input('Enter your amount to deposit: '))
        self.cbal = self.cbal + amount
        print(f'Your current balance after deposit is: {self.cbal}')

    def withdraw(self):
        amount = int(input('Enter your amount to withdraw: '))

        if self.cbal < amount:
            print('Insufficient balance')
        else:
            self.cbal = self.cbal - amount
            print(f'Current balance after withdrawal is: {self.cbal}')


c1 = ATM(123, 'Nandhini', 7433, 50000)

c1.check_balance()
c1.deposit()
c1.withdraw()'''

#student
'''class student:
    ssub='tamil'
    exam_hall=104
    total_mark=100

s1=student()
s1.sname='nandhini'
s1.mark=89
s1.grade='B'

s2=student()
s2.sname='nathiya'
s2.mark=91
s2.grade='A'

print(student.ssub,student.exam_hall,student.total_mark)
print(s1.sname,s1.mark,s1.grade)
print(s2.sname,s2.mark,s2.grade)'''

#STATIC METHODS
class ATM:
    bname = 'HDFC'
    bloc = 'Vel'
    bifsc = 'HDFC000'

    def __init__(self, cid, cname, cpin, cbal):
        self.cid = cid
        self.cname = cname
        self.cpin = cpin
        self.cbal = cbal

    def check_balance(self):
        upin = int(input('Enter your pin: '))

        if self.cpin == upin:
            print(f'Your current balance is: {self.cbal}')
        else:
            print('Invalid pin')

    def deposit(self):
        amount = int(input('Enter your amount to deposit: '))
        self.cbal = self.cbal + amount
        print(f'Your current balance after deposit is: {self.cbal}')

    @staticmethod
    def add(a,b):
        return a+b

    def withdraw(self):
        amount = int(input('Enter your amount to withdraw: '))

        if self.cbal < amount:
            print('Insufficient balance')
        else:
            self.cbal = self.cbal - amount
            print(f'Current balance after withdrawal is: {self.cbal}')


c1 = ATM(123, 'Nandhini', 7433, 50000)

c1.check_balance()
c1.deposit()
c1.withdraw()

class calculator:
    @staticmethod
    def add(a,b):
        return a+b

ob=calculator()
ob.add(10,20)


 
                  
