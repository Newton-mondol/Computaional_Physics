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

def f(x, fig):
    return fig(x);

#define a function which create a list of y0, y1, y2, y3............. for x, x+h, x+2h, x+3h............
def simpson(n, fig):
#     chose a value for h
    h=0.01;
    x = 0;
    x1 = [];
    y1 = [];
    odd = 0;
    even = 0;
    
    while x<n:
        x1.append(x)
        y1.append(f(x,fig));
        x = x+h;
    
    for i in range(1, len(y1)-1, 2):
        odd = odd + y1[i];
        
    p.for i in range(2, len(y1)-1, 2):
        even = even +y1[i];
    
    result = (h/3)*(y1[0] + 4*odd + 2*even + y1[len(y1)-1] );
    return result;
        
#----------------------work-space------------------------
x = simpson(10, np.sin);
print(x);
