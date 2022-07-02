from decimal import *
from math import *
getcontext().prec = 100000
getcontext().rounding = ROUND_HALF_DOWN

class PentaPyramidEncryption:
    def encry(self,s1,s2):
        a = int(s1)
        h = int(s2)
        asquare = (a * a)
        degree = radians(54)
        tangent = tan(degree)
        const = Decimal((Decimal(5) / Decimal(12)) * Decimal(tangent))
        cipher = Decimal(const * asquare * h).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        str_cipher = str(cipher)
        return str_cipher
