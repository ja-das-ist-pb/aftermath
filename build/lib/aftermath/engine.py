import numpy as np
from errors import MathInputError, MatrixSizeError, MatrixDimensionError, MatrixNotInvertibleError, VectorSizeError, VectorDimensionError



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
        raise TypeError("Input must be an integer")
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
        raise TypeError("Input must be an integer")
    if not isinstance(r, int):
        raise TypeError("Input must be an integer")
    if n<0 or r<0:
        raise MathInputError("Arguments must be ≥ 0")
    
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
        raise TypeError("Input must be an integer")
    if not isinstance(r, int):
        raise TypeError("Input must be an integer")
    if n<0 or r<0:
        raise MathInputError("Arguments must be ≥ 0")
    
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
        raise TypeError("Input must be a number (int or float)")
    if not isinstance(d, (int, float)):
        raise TypeError("Input must be a number (int or float)")
    if not isinstance(l, (int, float)):
        raise TypeError("Input must be a number (int or float)")
    if l<=0:
        raise MathInputError("Length of the series must be greater than 0")
    
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
        raise MathInputError("Length of the series must be greater than 0")
    elif r!=1:
        return a1*(1-r**l)/(1-r)
    else:
        return aser(a1, 0, int(l))

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
    """
    Add two matrices element-wise.

    Parameters:
    list1 (list of list of numbers): First input matrix.
    list2 (list of list of numbers): Second input matrix.

    Returns:
    list of list of numbers: Resulting matrix after addition.

    Raises:
    TypeError: If inputs are not lists.
    MatrixSizeError: If input matrices are not well-formed or have different dimensions.
    MathInputError: If matrix elements are not numeric.
    """

    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both inputs must be lists")
    
    alllength=len(list1[0])
    for i in list1:
        if len(i)!=alllength:
            raise MatrixSizeError("Input matrix is not well-formed. Each row must have the same number of elements")
    
    alllength=len(list2[0])
    for i in list2:
        if len(i)!=alllength:
            raise MatrixSizeError("Input matrix is not well-formed. Each row must have the same number of elements")
        
    arr1=np.array(list1)
    arr2=np.array(list2)

    if not np.issubdtype(arr1.dtype, np.number):
        raise MathInputError("Matrix elements must be numeric (int or float).")

    if not np.issubdtype(arr2.dtype, np.number):
        raise MathInputError("Matrix elements must be numeric (int or float).")
    
    if arr1.shape!=arr2.shape:
        raise MatrixSizeError("Matrices must have the same dimensions")

    return (arr1+arr2).tolist()


#matrix -- subtraction **(2d-list, 2d-list)
def msub(list1, list2):
    """
    Subtract the second matrix from the first matrix element-wise.

    Parameters:
    list1 (list of list of numbers): First input matrix.
    list2 (list of list of numbers): Second input matrix.

    Returns:
    list of list of numbers: Resulting matrix after subtraction.

    Raises:
    TypeError: If inputs are not lists.
    MatrixSizeError: If input matrices are not well-formed or have different dimensions.
    MathInputError: If matrix elements are not numeric.
    """
    
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both inputs must be lists")
    
    alllength=len(list1[0])
    for i in list1:
        if len(i)!=alllength:
            raise MatrixSizeError("Input matrix is not well-formed. Each row must have the same number of elements")
    
    alllength=len(list2[0])
    for i in list2:
        if len(i)!=alllength:
            raise MatrixSizeError("Input matrix is not well-formed. Each row must have the same number of elements")
        
    arr1=np.array(list1)
    arr2=np.array(list2)

    if not np.issubdtype(arr1.dtype, np.number):
        raise MathInputError("Matrix elements must be numeric (int or float).")

    if not np.issubdtype(arr2.dtype, np.number):
        raise MathInputError("Matrix elements must be numeric (int or float).")
    
    if arr1.shape!=arr2.shape:
        raise MatrixSizeError("Matrices must have the same dimensions")

    return (arr1-arr2).tolist()


#matrix -- product **(list, list), dimension of the list must over 1
def mpro(list1, list2):
    """
    Multiply two matrices using matrix multiplication rules.

    Parameters:
    list1 (list of list of numbers): First input matrix.
    list2 (list of list of numbers): Second input matrix.

    Returns:
    list of list of numbers: Resulting matrix after multiplication.

    Raises:
    TypeError: If inputs are not lists.
    MatrixSizeError: If matrices are not well-formed or have incompatible dimensions for multiplication.
    MathInputError: If matrix elements are not numeric.
    """
    
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Both inputs must be lists")
    
    alllength=len(list1[0])
    for i in list1:
        if len(i)!=alllength:
            raise MatrixSizeError("Input matrix is not well-formed. Each row must have the same number of elements")

    alllength=len(list2[0])   
    for i in list2:    
        if len(i)!=alllength:
            raise MatrixSizeError("Input matrix is not well-formed. Each row must have the same number of elements")
        
    arr1=np.array(list1)
    arr2=np.array(list2)

    if not np.issubdtype(arr1.dtype, np.number):
        raise MathInputError("Matrix elements must be numeric (int or float).")

    if not np.issubdtype(arr2.dtype, np.number):
        raise MathInputError("Matrix elements must be numeric (int or float).")
    
    if len(list2)!=len(list1[0]):
        raise MatrixSizeError("Cannot multiply matrices: number of columns in the first matrix does not match number of rows the second matrix")
    
    return (np.matmul(arr1, arr2)).tolist()


#vector -- dot product **(1d-list, 1d-list)
def vdot(list1, list2):
    """
    Calculate the dot product of two vectors.

    Parameters:
    list1 (list of numbers): First input vector.
    list2 (list of numbers): Second input vector.

    Returns:
    float: Dot product of the two vectors.

    Raises:
    TypeError: If inputs are not lists.
    VectorSizeError: If vectors have different lengths.
    VectorDimensionError: If inputs are not 1D lists.
    MathInputError: If vector elements are not numeric.
    """
    if not isinstance(list1, list):
        raise TypeError("Input must be a list")

    if not isinstance(list2, list):
        raise TypeError("Input must be a list")
    
    if len(list1)!=len(list2):
        raise VectorSizeError("Input vectors is not well-formed. Vectors must have the same number of dimensions")
        
    arr1=np.array(list1)
    arr2=np.array(list2)

    if not np.issubdtype(arr1.dtype, np.number):
        raise MathInputError("Matrix elements must be numeric (int or float).")

    if not np.issubdtype(arr2.dtype, np.number):
        raise MathInputError("Matrix elements must be numeric (int or float).")
    
    if arr1.ndim!=1:
        raise VectorDimensionError("Vector must be a 1-dimensional list")
    
    return np.dot(arr1, arr2)


#matrix -- determinant **(2d-list)
def mdet(list):
    """
    Calculate the determinant of a square matrix.

    Parameters:
    list (list of list of numbers): Input square matrix.

    Returns:
    float: Determinant of the matrix.

    Raises:
    TypeError: If input is not a list.
    MatrixSizeError: If the matrix is not square or not well-formed.
    MatrixDimensionError: If input is not a 2D matrix.
    MathInputError: If matrix elements are not numeric.
    """
    if not isinstance(list, list):
        raise TypeError("Input must be a list")
    
    alllength=len(list[0])
    for i in list:
        if len(i)!=alllength:
            raise MatrixSizeError("Input matrix is not well-formed. Each row must have the same number of elements")
    
    arr=np.array(list)
    
    if not np.issubdtype(arr.dtype, np.number):
        raise MathInputError("Matrix elements must be numeric (int or float).")
    
    if arr.ndim!=2:
        raise MatrixDimensionError("Input must be a 2D matrix")

    if arr.shape[0]!=arr.shape[1]:
        raise MatrixSizeError("Matrix must be square (same number of rows and columns)")
    
    return np.linalg.det(arr)


#matrix -- inverse **(2d-list, 2d-list)
def minv(list):
    """
    Calculate the inverse of a square matrix.

    Parameters:
    list (list of list of numbers): Input square matrix.

    Returns:
    list of list of numbers: Inverse of the matrix.

    Raises:
    TypeError: If input is not a list.
    MatrixSizeError: If the matrix is not square or not well-formed.
    MatrixDimensionError: If input is not a 2D matrix.
    MathInputError: If matrix elements are not numeric.
    MatrixNotInvertibleError: If the matrix is singular (determinant is zero).
    """
    if not isinstance(list, list):
        raise TypeError("Input must be a list")
    
    alllength=len(list[0])
    for i in list:
        if len(i)!=alllength:
            raise MatrixSizeError("Input matrix is not well-formed. Each row must have the same number of elements")
        
    arr=np.array(list)
    
    if not np.issubdtype(arr.dtype, np.number):
        raise MathInputError("Matrix elements must be numeric (int or float).")
    
    if arr.ndim!=2:
        raise MatrixDimensionError("Input must be a 2D matrix")
    
    if arr.shape[0]!=arr.shape[1]:
        raise MatrixSizeError("Matrix must be square (same number of rows and columns)")
    
    if np.linalg.det(arr)==0:
        raise MatrixNotInvertibleError("Matrix is singular and cannot be inverted because its determinant is zero")
    
    return (np.linalg.inv(arr)).tolist()