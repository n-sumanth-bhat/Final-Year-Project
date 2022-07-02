from decimal import *
from math import sqrt
getcontext().prec = 100000
getcontext().rounding = ROUND_HALF_DOWN

#Volume
class HexaPrismEncryption:
    def encry(self,s1,s2):
        a = int(s1)
        h = int(s2)
        asquare = (a * a)
        d = Decimal(3)
        numerator = Decimal(3 * d.sqrt() * asquare * h)
        cipher = Decimal(Decimal(numerator) / Decimal(2)).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        str_cipher = str(cipher)
        return str_cipher

