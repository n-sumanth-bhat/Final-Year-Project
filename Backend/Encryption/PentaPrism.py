from decimal import *
from math import sqrt
getcontext().prec = 100000
getcontext().rounding = ROUND_HALF_DOWN

#Volume
class PentaPrismEncryption:
    def encry(self,s1 , s2):
        a = int(s1)
        h = int(s2)
        asquare = (a * a)
        const = Decimal(sqrt(5 * (5 + (2 * sqrt(5)))))
        numerator = Decimal(const * asquare * h)
        cipher = Decimal(Decimal(numerator) / Decimal(4)).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        str_cipher = str(cipher)
        return str_cipher
