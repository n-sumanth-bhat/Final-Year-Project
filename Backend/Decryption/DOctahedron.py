from decimal import *
from math import *

class OctahedronDecryption:
    def Adecry(self,cipher,key):
        m = int(key)
        cipher = int(cipher)
        b = int(m ** 2)
        h1 = int(int(3) * cipher)
        h2 = int(b * int(2))
        h = Decimal(Decimal(h1) / Decimal(h2)).quantize(Decimal(1.00),ROUND_HALF_DOWN)
        ascii = str(Decimal(str(key)+ str(h)).quantize(Decimal(1.00),ROUND_HALF_DOWN))
        #print("Ascii newly calculated is",ascii)
        return [key,h]

    def A2decry(self,cipher,key):
        c = int(cipher)
        a_square = int(key)
        numerator = int(int(3) * c)
        denominator = int(a_square * int(2))
        h = Decimal(Decimal(numerator) / Decimal(denominator)).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        d = Decimal(key)
        a = Decimal(d.sqrt()).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        ascii = str(str(a) + str(h))
        return [a,h]

    def Hdecry(self,cipher,key):
        c = int(cipher)
        h = int(key)
        numerator = int(int(3) * c)
        denominator = int(h * int(2))
        a_square = Decimal(Decimal(numerator) / Decimal(denominator)).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        d = Decimal(a_square)
        a = Decimal(d.sqrt()).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        ascii = str(str(a) + str(h))
        return [a,h]


