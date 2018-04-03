def my_func(x):
    return x**100 -100

def my_derivat_fun(x):
    return 100*x**99  


def xn (x):
    return x - (my_func(x))/(my_derivat_fun(x))

xinit = 1.81
for i in range(109):
    xinit = xn(xinit)
    print(xinit)



