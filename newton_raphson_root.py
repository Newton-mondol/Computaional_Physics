# Determine value of a algebraic function at any point
def f_value(fun, arg):
    return fun(arg)


# Value of derivative of a funtion at any given point
# Here we have used h = 0.00001
def deri(f, arg):
    return (f_value(f, arg + 0.00001) - f_value(f, arg)) / 0.00001


# Determination of root around any point using Newton-Raphson root finding mathod
def n_r_root(fun, arg):
    for i in range(100):
        arg = arg - (f_value(fun, arg) / deri(fun, arg))
    return round(arg, 2)

