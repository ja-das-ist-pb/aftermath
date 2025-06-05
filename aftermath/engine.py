import numpy as np

#constant -- pi
pi=3.1415926535897932

#constant -- e
e=2.7182818284590452

#basic calculation -- power
def pow(a, n):
    ...

#discrete mathematics -- factorial
def fac(n):
    tot=1
    for i in range(2, n+1):
        tot*=i
    return tot

#discrete mathematics -- permutation
def p(n, r):
    return fac(n)//fac(r)

#discrete mathematics -- combination
def c(n, r):
    return fac(n)//fac(r)*fac(n-r)

#arithmetic series ** ase("a1", common "d"ifference, "l"ength)
def ase(a1, d, l):
    return (2*a1+(l-1)*d)//2

#geometric series ** gse("a1", common "r"atio, "l"ength)
def gse(a1, r, l):
    return a1*(1-pow(r, l))//(1-a1)

#radian to degree transformation
def rtd(r):
    return r*180/pi

#degree to radian transformation
def dtr(d):
    return d*pi/180

#trigonometric -- sin 
def sin(x):
    ...

#trigonometric -- cos
def cos(x):
    ...

#trigonometric -- tan
def tan(x):
    ...

#trigonometric -- csc
def csc(x):
    ...

#trigonometric -- sec
def sec(x):
    ...

#trigonometric -- cot
def cot(x):
    ...

#trigonometric -- arcsin
def arcsin(x):
    ...

#trigonometric -- arccos
def arccos(x):
    ...

#trigonometric -- arctan
def arctan(x):
    ...

#trigonometric -- arccsc
def arccsc(x):
    ...

#trigonometric -- arcsec
def arcsec(x):
    ...
#trigonometric -- arccot
def arccot(x):
    ...

#nature exponential
def nex(n):
    return pow(e, n)

#nature logarithm
def ln(n):
    ...

#logarithm **(base, argument)
def log(b, a):
    return ln(a)/ln(b)

#matrix -- addition **(2d-list, 2d-list)
def madd(list1, list2):
    arr1=np.array(list1)
    arr2=np.array(list2)
    return (arr1-arr2).tolist()


#matrix -- subtraction **(2d-list, 2d-list)
def msub(list1, list2):
    arr1=np.array(list1)
    arr2=np.array(list2)
    return (arr1-arr2).tolist()


#matrix -- product **(2d-list, 2d-list)
def mpro(list1, list2):
    arr1=np.array(list1)
    arr2=np.array(list2)
    n, m=arr1.shape
    pro=np.empty((n, m))
    for i in range(n):
        for j in range(m):
            pro[i][j]=arr1[i][j]*arr2[j][i]
    return pro.tolist()

#matrix -- determinant **(2d-list, 2d-list)
def mdet(list):
    ...

#matrix -- inverse **(2d-list, 2d-list)
def minv(list):
    ...