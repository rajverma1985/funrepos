class Test:
    def __init__(self, **kwargs):
        print(kwargs)


t = Test(val1=1, val2=3)
t1 = Test(name='raj', last='verma')
