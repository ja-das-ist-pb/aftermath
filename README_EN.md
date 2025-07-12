**aftermath**

aftermath is a Python mathematical module developed by Zhong-Zheng Senior High School students.  
This repository provides detailed usage in both English and Chinese.  
(You are reading the English version: README_EN.md)

---

**Installation**

Install via pip:

pip install aftermath

Or clone and install manually:

git clone https://github.com/ja-das-ist-pb/aftermath.git
cd aftermath
pip install .

---

**Features & Usage Examples**

**Constants**

from aftermath import pi, e

print(f"Pi: {pi}")  # 3.1415926535897932
print(f"Euler's number (e): {e}")  # 2.7182818284590452

**Factorial**

from aftermath import fac

n = 5
print(f"{n}! = {fac(n)}")  # 120

**Permutations**

from aftermath import p

n, r = 5, 3
print(f"P({n}, {r}) = {p(n, r)}")  # 60

**Combinations**

from aftermath import c

n, r = 5, 3
print(f"C({n}, {r}) = {c(n, r)}")  # 10

**Arithmetic Series Sum**

from aftermath import aser

a1, d, l = 2, 3, 5
print(f"Arithmetic series sum: {aser(a1, d, l)}")  # 40.0

**Geometric Series Sum**

from aftermath import gser

a1, r, l = 3, 2, 4
print(f"Geometric series sum: {gser(a1, r, l)}")  # 45.0

**Angle Conversions**

from aftermath import rtod, dtor

radian = 3.14159
degree = 180

print(f"{radian} radians = {rtod(radian)} degrees")  # ≈180.0
print(f"{degree} degrees = {dtor(degree)} radians")  # ≈3.14159

---

**Matrix Operations**

from aftermath import madd, msub, mpro, mdet, minv

a = [[1, 2],
     [3, 4]]
b = [[5, 6],
     [7, 8]]

print("Addition:", madd(a, b))  
# Output: [[6, 8], [10, 12]]

print("Subtraction:", msub(b, a))  
# Output: [[4, 4], [4, 4]]

print("Multiplication:", mpro(a, b))  
# Output: [[19, 22], [43, 50]]

print("Determinant of a:", mdet(a))  
# Output: -2.0

print("Inverse of a:", minv(a))  
# Output: [[-2.0, 1.0], [1.5, -0.5]]

---

**Vector Operations**

from aftermath import vdot

v1 = [1, 2, 3]
v2 = [4, 5, 6]

print(f"Dot product: {vdot(v1, v2)}")  # 32

---

**Error Handling**

Custom exceptions are provided in aftermath.errors:

- MathInputError: Input value errors
- MatrixSizeError: Matrix dimension mismatch or malformed
- MatrixDimensionError: Invalid matrix dimensions
- MatrixNotInvertibleError: Matrix not invertible (determinant zero)
- VectorSizeError: Vector length mismatch
- VectorDimensionError: Vector dimension error (not 1D)

Example:

from aftermath import mdet
from aftermath.errors import MatrixSizeError

try:
    mdet([[1, 2], [3]])
except MatrixSizeError as e:
    print("Matrix format error:", e)

---

**Requirements**

- Python 3.7 or higher  
- numpy package

---

**License**

MIT License

---

**Zhong-Zheng Senior High School Mathematics Module Development Team--GOD PB**