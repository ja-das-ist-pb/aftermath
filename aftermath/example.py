from engine import *

while True:
    s=input()
    if s.capitalize()=="EXIT":
        break
    else:
        print(eval(s))
    