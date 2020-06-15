a = bool(True) == True                   # True
b = bool(False) == False                 # True
c = True == True                         # True
d = True != False                        # True
e = True or False                        # True
f = True and False                       # False
g = bool(bool(False) == False) or False  # True
h = bool(False) is not bool(False)       # False

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)