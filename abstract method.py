'''from abc import ABC ,abstractmethod

class sample1(ABC):
    @abstractmethod
    def msg1(self):
        pass

    @abstractmethod
    def msg2(self):
        pass


class sample2(sample1):
    def msg1(self):
        print('hi hellooo')


    def msg2(self):
        print('good morning ')


s2=sample2()
s2.msg1()
s2.msg2()
'''


#abs class using atm

from abc import ABC ,abstractmethod

class ATM(ABC):
    @abstractmethod
    def check_bal(self):
        pass

    @abstractmethod
    def deposite(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass


class new_ATM(ATM):


    def __init__(self,cid,cname,cpin,cbal):
        self.cid=cid
        self.cname=cname
        self.cpin=cpin
        self.cbal=cbal
        
    def check_bal(self):
        upin=int(input('enter your pin:'))
        if upin==self.cpin:
            print(f'your cuurent balance is:{self.cbal}')
        else:
            print('invalid pin')


    def deposite(self):
        amount=int(input('enter a depositing amount :'))
        self.cbal=self.cbal+amount
        print(f'your current balance deposite is:{self.cbal}')
        


    def withdraw(self):
        amount=int(input('enter a withdraw amount :'))
        if self.cbal>amount:
            self.cbal=self.cbal-amount
            print(f'after withdraw:{self.cbal}')
        else:
            print(f'insufficient balance')
        

n2=new_ATM(123,'nan',1234,50000)
n2.check_bal()
n2.deposite()
n2.withdraw()

        
    


    
