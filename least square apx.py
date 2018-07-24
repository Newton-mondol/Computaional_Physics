#about to done#
from pylab import*
from numpy import*
m = int(input("Enter number of data: "))
l1 = []
l2 = []
b = 0
a = 0
print("Input x values")
while True:
    x = float(input(">> "))
    l1 = l1 + [x]
    a = a + 1
    if a == m:
        break
print('x values are: {}'.format(l1))
print("Input y values")
while True:
    y = float(input(">> "))
    l2 = l2 + [y]
    b = b + 1
    if b == m:
        break
print('y values are: {}'.format(l2))
n = sum(l1)
p = sum(l2)
l3 = [i*i for i in l1]
q = sum(l3)
l4 = [i*j for i,j in zip(l1, l2)]
r = sum(l4)
a_0 = (r*n - p*q) / (n*n - q*m)
a_1 = (p - a_0 * m) / n
x = arange(min(l1) - 2, max(l2) + 1, 0.5)
y = a_0 + a_1*x
plot(x, y)
plot(l1, l2, 'ro')
axis([min(l1) - 1, max(l1) + 1, min(l2) - 1, max(l2) + 1])
show()
