from decimal import *
from math import *

class PentaPyramidDecryption:
    def Adecry(self,cipher,key):
        a = int(key)
        c = int(cipher)
        a_square = (a * a)
        degree = radians(54)
        tangent = tan(degree)
        numerator = Decimal(12 * c)
        denominator = Decimal(Decimal(5) * Decimal(tangent) * Decimal(a_square))
        h = Decimal(Decimal(numerator) / Decimal(denominator)).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        ascii = str(str(a) + str(h))
        return [a,h]

    def A2decry(self,cipher,key):
        a_square = int(key)
        c = int(cipher)
        degree = radians(54)
        tangent = tan(degree)
        numerator = Decimal(12 * c)
        denominator = Decimal(Decimal(5) * Decimal(tangent) * Decimal(a_square))
        h = Decimal(Decimal(numerator) / Decimal(denominator)).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        d = Decimal(a_square)
        a = Decimal(d.sqrt()).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        ascii = str(str(a) + str(h))
        return [a,h]
    
    def Hdecry(self,cipher,key):
        h = int(key)
        c = int(cipher)
        degree = radians(54)
        tangent = tan(degree)
        numerator = Decimal(12 * c)
        denominator = Decimal(Decimal(5) * Decimal(tangent) * Decimal(h))
        a_square = Decimal(Decimal(numerator) / Decimal(denominator)).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        d = Decimal(a_square)
        a = Decimal(d.sqrt()).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        ascii = str(str(a) + str(h))
        return [a,h]
