class bank:
    bname='hdfc'
    bloc='velachery'
    __brevenue=3000000
    def __init__(self,cid,cname,cloc):
        self.cid=cid
        self.cname=cname
        self.cloc=cloc

    def __display(self):
        print(self.cid,self.cname,self.cloc)



    #getter method
    @classmethod
    def get_revenue(cls):
        return cls.__brevenue

    #settermethod
    @classmethod
    def set_brevenue(clas,new_rev):
        cls.__brevenue=new_rev


c1=bank(123,'nandhu','velachery')
print(bank.get_revenue())
bank.set_brevenue
