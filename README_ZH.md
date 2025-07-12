**aftermath**

aftermath 是由中正高中學生開發的 Python 數學模組。  
本專案提供完整中文與英文說明，這裡為中文版本：README_ZH.md

---

**安裝方式**

使用 pip 安裝：

pip install aftermath

或手動安裝：

git clone https://github.com/ja-das-ist-pb/aftermath.git
cd aftermath
pip install .

---

**功能與使用說明**

**常數**

from aftermath import pi, e

print(f"圓周率 π: {pi}")
print(f"歐拉數 e: {e}")

**階乘**

from aftermath import fac

n = 5
print(f"{n}! = {fac(n)}")  # 120

**排列數**

from aftermath import p

n, r = 5, 3
print(f"P({n}, {r}) = {p(n, r)}")  # 60

**組合數**

from aftermath import c

n, r = 5, 3
print(f"C({n}, {r}) = {c(n, r)}")  # 10

**等差級數**

from aftermath import aser

a1, d, l = 2, 3, 5
print(f"等差級數: {aser(a1, d, l)}")  # 40.0

**等比級數**

from aftermath import gser

a1, r, l = 3, 2, 4
print(f"等比級數: {gser(a1, r, l)}")  # 45.0

**角度轉換**

from aftermath import rtod, dtor

radian = 3.14159
degree = 180

print(f"{radian} 弧度 = {rtod(radian)} 度")  # 約180.0
print(f"{degree} 度 = {dtor(degree)} 弧度")  # 約3.14159

---

**矩陣運算**

from aftermath import madd, msub, mpro, mdet, minv

a = [[1, 2],
     [3, 4]]
b = [[5, 6],
     [7, 8]]

print("矩陣加法:", madd(a, b))  
# 輸出: [[6, 8], [10, 12]]

print("矩陣減法:", msub(b, a))  
# 輸出: [[4, 4], [4, 4]]

print("矩陣乘法:", mpro(a, b))  
# 輸出: [[19, 22], [43, 50]]

print("矩陣行列式:", mdet(a))  
# 輸出: -2.0

print("矩陣反方陣:", minv(a))  
# 輸出: [[-2.0, 1.0], [1.5, -0.5]]

---

**向量運算**

from aftermath import vdot

v1 = [1, 2, 3]
v2 = [4, 5, 6]

print(f"內積: {vdot(v1, v2)}")  # 32

---

**錯誤處理**

本模組在 aftermath.errors 中提供自訂錯誤類別：

- MathInputError：輸入數值錯誤
- MatrixSizeError：矩陣維度不符或格式錯誤
- MatrixDimensionError：矩陣維度錯誤
- MatrixNotInvertibleError：矩陣不可逆（行列式為零）
- VectorSizeError：向量長度不符
- VectorDimensionError：向量維度錯誤（非一維）

範例：

from aftermath import mdet
from aftermath.errors import MatrixSizeError

try:
    mdet([[1, 2], [3]])
except MatrixSizeError as e:
    print("矩陣格式錯誤:", e)

---

**系統需求**

- Python 3.7 或以上版本  
- numpy 套件

---

**授權條款**

MIT 授權

---

**Zhong-Zheng Senior High School Mathematics Module Development Team--GOD PB**