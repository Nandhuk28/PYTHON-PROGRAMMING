'''def facebook(func):
    def inner (*args,**kwargs):
        print('www.facebook.com')
        print('login')
        func(*args,**kwargs)
        print('logout')
    return inner
@facebook
def update_profile(name):
    print(f'photo updated for:{name} account')
update_profile('nandhu')
@facebook
def update_story(name):
    print(f'story updated for:{name} account')
update_profile('nathiya')'''

#wap to delay the execution of function by n number of seconds       *imp

'''def delay(func):
    def inner(*args,**kwargs):
        import time
        time.sleep(10)
        func(*args,**kwargs)

    return  inner
@delay
def sample(name):
    print(f'good afternoon :{name}')

sample('vasanth')
'''

# wap to check the execution time of another function using decorator            * imp

def ex_time(func):
    def inner(*args,**kwargs):
        import time
        st=time.time()
        func(*args,**kwargs)
        et=time.time()
        print(f'time taken for ex is: {et-st}')
    return inner

@ex_time

def sam():
    for i in range(1,20):
        print(i)

sam()
