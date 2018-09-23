# Matrix operation
# using matrix find value of the variable in linear system of equation
# linear equation look----> ax + by + c = 0
# now consider a system of equation 
#
#  a00*x0 + a01*x2 + a02*x2+...........+a0n*xn = b0
#  a10*x0 + a11*x2 + a12*x2+...........+a1n*xn = b1
#  a20*x0 + a21*x2 + a22*x2+...........+a2n*xn = b2
#  ................................................
#  ................................................
#  ................................................
#  an0*x0 + an1*x2 + an2*x2+...........+ann*xn = bn
#
# from this system of linear equation I write  it in matrix form like
#
#   a00  a01  a02  ......... a0n 
#   a10  a11  a12  ......... a1n 
#   a20  a21  a22  ......... a2n 
#   a30  a31  a32  ......... a3n 
#   ............................ 
#   ............................ 
#   an0  an1  an2  ......... ann 
#
#---------------------------------------------
#   upper triangular Matrix 
#
#          j   j+1  j+2            j+n
#
#   i-->  a00  a01  a02  ......... a0n 
#  i+1--> 0  a11  a12  .........  a1n   --0
#  i+2--> 0   0  a12  .........   a1n   --1 ----->number of 0's
#  i+3--> 0   0   0  ...........  a2n   --2
#         ............................ 
#         ............................ 
#  i+n--> 0   0   0  0  0......   ann
#
#     (n-1)-0 (n-1)-1 (n-1)-2 -------------> number of 0's
#
#   so each element can access by a[i][j] where i = row_number and j = colm_number
#
#  so my target is now  form a10 = 0 , a20 = 0, a21 = 0, a30 = 0, a31 = 0 ................., a(n-1)n = 0
#  so if I want a10  = 0  using (r2 - r1) row operation
# 
#    r2 - r1 = (a10 +  a11 + a12 + ...) - (a00 + a01 + a02 + .....)*(a10/a00)
#    r2 - r1 = a10 - a00*(a10/a00) + a11 - a01*(a10/a00) + ....
#                            
#                            a10                     a10
#                    a[0][j]------         a[0][j+1]------   ,where j = colum number
#                            a00                     a00
#
#  we multiply r1 (row 1) each colum element( from j to j+n ) by 
#
#                a10
#     a[0][j]*  -----
#                a00
#
#  but if I want to a20 = 0 using (r3 - r1) row operation
#  we multiply r1 (row 1) each colum element (from j to j+n) by
#
#                a20
#    a[0][j]*   ------
#                a00
#
#  so for row tracking like (r2-r1), (r3-r1), (r4-r1) .......
#  I change the value 
#              a[i][0]
#    a[0][j]* ---------  where i = row number
#                a00
#   
#   this operation make the first colum (j=0) element ( without r1) to 0 
#   But what about the other colum ? if we want j+1 colum element(without r1 and r2) to 0 ...
#   so the process graphically look like
#
#  a00 
#  |------------------  { this process run n-1 times}  m=0
#  0  |---------------  { this process run n-1 times}  m=1  , where n is the number of row
#  0  0  |------------  { this process run n-1 times}  m=2
#  0  0  0 ...........                                            
#  0  0  0 ...........
#  0  0  0 ..........|-->ann
#                                                   a[i][m] 
#  so the formula is a[i][j] = a[i][j] - a[m][j] * ---------
#                                                   a[m][m]
#------------------------------------------
# 

def f(a):
    new_arr = [];
    
    for m in range(len(a)-1):
        for i in range(m+1, len(a)): # row accessing loop
            x = a[i][m];
            for j in range(m, len(a)): # colum accessing loop
                
                a[i][j] = a[i][j] - (a[m][j] * x/a[m][m]);
                

    return a;
    
a = [[1,2,-4],
     [2,3,6],
     [3,2,1]]
print(f(a));    
    
