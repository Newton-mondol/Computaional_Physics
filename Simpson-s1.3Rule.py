
import numpy as np;
# simpson's 1/3 rule
#
#                        i = 1                      j= 2
#            list[0]     list[i]                    list[j]                 list[len(list)-1]
#                        i=i+2                      j=j+2
#
#                        last term (n-1)            last term (n-2)
#                        (n-2) < (n-1) < n
#
# f(x) = (h/3)*(y0 + 4*(y1+ y3 + y5 +....+yn-1) +2*(y2 + y4 + y6 +...+yn-2) + yn)
#
#

# define a function which get (x , fig) and return y = f(x)
#
# convert degree--->radian (pi/180) if fig = sin, cos, tan, cot

def f(x, fig):
    if fig == np.sin or fig == np.cos:
        x = (np.pi * x) / 180;
    return fig(x);


# define a function which create a list of y0, y1, y2, y3............. for x, x+h, x+2h, x+3h............
# a is the start point,
# b is the end point,
# n is the number of division
def simpson(a, b, n, fig):
    h = n;
    x = a;
    x1 = [];
    y1 = [];
    odd = 0;
    even = 0;

    while x <= b:
        x1.append(x)
        y1.append(f(x, fig));
        x = x + h;

    for i in range(1, len(y1) - 1, 2):
        odd = odd + y1[i];  # finding (y1+ y3+ y5+ ....)

    for i in range(2, len(y1) - 1, 2):
        even = even + y1[i];  # finding (y2+ y4+ y6+ ....)

    result = (h / 3) * (y1[0] + 4 * odd + 2 * even + y1[len(y1) - 1]);
    return result;


# --------------user place-------------------------

def x2(x):
    return x*x;

print("Integration of x^2 with lower limit 1 upper limit 10 interval .001 is: ",simpson(1,10,.001, x2),"\n");
print("Integration of sin(x) with lower limit 0 upper limit 90 interval .001 is: ",simpson(0, 90, 0.001, np.sin),"\n");
print("Integration of cos(x) with lower limit 0 upper limit 90 interval .001 is: ",simpson(0,90,0.001,np.cos));
