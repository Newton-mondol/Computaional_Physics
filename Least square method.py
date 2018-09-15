def listSquare(arrX, arrY):
#     define and initilize c1, c2, c3, c4
    c1 = 0;
    c2 = 0;
    c3 = 0;
    c4 = 0;
    
#     c1 =  Σ arrX[i]
#     c2 =  Σ arrX[i]^2
#     c3 =  Σ arrY[i]
#     c4 =  Σ arrX[i] x arrY[i]
    
    for i in range(len(arrX)):
        c1 = c1 + arrX[i];
        c2 = c2 + (arrX[i]*arrX[i]);
        c3 = c3 + arrY[i];
        c4 = c4 + (arrX[i]*arrY[i]);
        
#     now find a0 and a1 where n = len(arrX) is the length of arrX
#            
#             (c1*c4) - (c2*c3)
#     a0 = -----------------------
#             (c1^2) - (n*c2)
#

# 
#              (c1*c3) - (n*c4)
#     a1 = ------------------------
#             (c1^2) - (n*c2)

    den = (c1*c1) - (len(arrX)*c2);
    
    a0 = ((c1*c4) - (c2*c3))/den;
    
    a1 = ((c1*c3) - (len(arrX)*c4))/den;
    
    
#     define a function which calculate y = a1*x + a0
    def f(x):
        return a0 + (a1*x);
    
#   new calculated y_f (using least squere mathod ) is define and initilize as 0  
    y_f = [0, 0, 0, 0];
    
#   calculating y_f using a0 and a1   
    for i in range(len(y_f)):
        y_f[i] = f(arrX[i]);
    
    return y_f;
    
