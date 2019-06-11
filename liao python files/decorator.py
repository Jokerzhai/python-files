def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

    
def log2(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s(): ' % (text,func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log    
def now():
    print('2015-3-25')


@log2('execute')
def now1():
    print('2016-3-25')

now()
now1()