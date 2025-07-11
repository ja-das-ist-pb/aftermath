import numpy as np
from errors import MathInputError, MathListSizeError



#constant -- pi
pi=3.1415926535897932

#constant -- e
e=2.7182818284590452

#factorial, only for integers
def fac(n):
    """
    Calculate the factorial of n, where n must be a non-negative integer.

    Parameters:
    n (int): The integer to calculate the factorial for.

    Returns:
    int: The factorial of n.

    Raises:
    TypeError: If n is not an integer.
    MathInputError: If n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be a Integer")
    if n==0:
        return 1
    elif n<0:
        raise MathInputError("Factorial input must be ≥ 0")
    
    tot=1
    for i in range(2, n+1):
        tot*=i
    return tot

#discrete mathematics -- permutation
def p(n, r):
    """
    Calculate the number of permutations of n items taken r at a time.

    Parameters:
    n (int): Total number of items.
    r (int): Number of items to arrange.

    Returns:
    int: Number of permutations.

    Raises:
    TypeError: If n or r is not an integer.
    MathInputError: If n or r is negative.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be a Integer")
    if not isinstance(r, int):
        raise TypeError("Input must be a Integer")
    if n<0 or r<0:
        raise MathInputError("Arguements must be ≥ 0")
    
    return fac(n)//fac(n-r)

#discrete mathematics -- combination
def c(n, r):
    """
    Calculate the number of combinations of n items taken r at a time.

    Parameters:
    n (int): Total number of items.
    r (int): Number of items to choose.

    Returns:
    int: Number of combinations.

    Raises:
    TypeError: If n or r is not an integer.
    MathInputError: If n or r is negative.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be a Integer")
    if not isinstance(r, int):
        raise TypeError("Input must be a Integer")
    if n<0 or r<0:
        raise MathInputError("Arguements must be ≥ 0")
    
    return fac(n)//(fac(r)*fac(n-r))

#arithmetic series ** ase("a1", common "d"ifference, "l"ength)
def aser(a1, d, l):
    """
    Calculate the sum of an arithmetic series.

    Parameters:
    a1 (int or float): The first term of the series.
    d (int or float): The common difference.
    l (int or float): The number of terms.

    Returns:
    float: The sum of the arithmetic series.

    Raises:
    TypeError: If inputs are not numbers.
    MathInputError: If length l is not greater than 0.
    """
    if not isinstance(a1, (int, float)):
        raise TypeError("Input must be a Integer")
    if not isinstance(d, (int, float)):
        raise TypeError("Input must be a Integer")
    if not isinstance(l, (int, float)):
        raise TypeError("Input must be a Integer")
    if l<=0:
        raise MathInputError("the length of the series must be > 0")
    
    return (2*a1+(l-1)*d)*l/2

#geometric series ** gse("a1", common "r"atio, "l"ength)
def gser(a1, r, l):
    """
    Calculate the sum of a geometric series.

    Parameters:
    a1 (int or float): The first term of the series.
    r (int or float): The common ratio.
    l (int or float): The number of terms.

    Returns:
    float: The sum of the geometric series.

    Raises:
    TypeError: If inputs are not numbers.
    MathInputError: If length l is not greater than 0.
    """
    if not isinstance(a1, (int, float)):
        raise TypeError("Input must be a number (int or float)")
    if not isinstance(r, (int, float)):
        raise TypeError("Input must be a number (int or float)")
    if not isinstance(l, (int, float)):
        raise TypeError("Input must be a number (int or float)")
    if l<=0:
        raise MathInputError("the length of the series must be > 0")
    elif r!=1:
        return a1*(1-r**l)/(1-r)
    else:
        return aser(a1, 0, l)

#radian to degree transformation
def rtod(r):
    """
    Convert an angle from radians to degrees.

    Parameters:
    r (int or float): Angle in radians.

    Returns:
    float: Angle in degrees, normalized to [0, 360).

    Raises:
    TypeError: If input is not a number.
    """
    if not isinstance(r, (int, float)):
        raise TypeError("Input must be a number (int or float)")
    return (r*180/pi)%360

#degree to radian transformation
def dtor(d):
    """
    Convert an angle from degrees to radians.

    Parameters:
    d (int or float): Angle in degrees.

    Returns:
    float: Angle in radians, normalized to [0, 2π).

    Raises:
    TypeError: If input is not a number.
    """
    if not isinstance(d, (int, float)):
        raise TypeError("Input must be a number (int or float)")
    return (d*pi/180)%(2*pi)



#matrix -- addition **(2d-list, 2d-list)
def madd(list1, list2):
    arr1=np.array(list1)
    arr2=np.array(list2)
    return (arr1+arr2).tolist()


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