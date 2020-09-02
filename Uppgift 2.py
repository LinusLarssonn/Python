import math

def kostnad(P, r, a):
    k = P + (a+1)*P*r/2
    print("Den totala kostnaden efter", a, "år blir", int(k), "kronor")

kostnad(500030, 0.03, 10)