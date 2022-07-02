from decimal import *
from math import *
getcontext().prec = 100000
getcontext().rounding = ROUND_HALF_DOWN

#Volume
class OctaPrismEncryption():
    def encry(self,s1,s2):
        a = int(s1)
        h = int(s2)
        asquare = (a * a)

        const = Decimal(2 * (1 + Decimal(2).sqrt()))
        cipher = Decimal(const * asquare * h).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        str_cipher = str(cipher)
        return str_cipher




