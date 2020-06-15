A = bool(True) == True                   # True
B = bool(False) == False                 # True
C = True == True                         # True
D = True != False                        # True
E = True or False                        # True
F = True and False                       # False
G = bool(bool(False) == False) or False  # True
H = bool(False) is not bool(False)       # False

print(A)
print(B)
print(C)
print(D)
print(E)
print(F)
print(G)
print(H)

I = None is None                                                                        # True
J = None is not None                                                                    # False
K = bool(bool(None) is not bool(None)) == False                                         # True
L = (bool(bool(None) is not bool(None)) == False and bool(None))                        # False
M = (bool(bool(None) is not bool(None)) == False and bool(None)) and (None is not None) # False

print(I)
print(J)
print(K)
print(L)
print(M)