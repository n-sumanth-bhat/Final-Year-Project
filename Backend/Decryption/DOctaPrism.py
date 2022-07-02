from decimal import *
from math import *

class OctaPrismDecryption:
    def Adecry(self,cipher,key):
        a = int(key)
        c = int(cipher)
        a_square = (a * a)
        const = Decimal(2 * (1 + Decimal(2).sqrt()))
        denominator = Decimal(const * a_square)
        h = Decimal(Decimal(c) / Decimal(denominator)).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        ascii = str(str(a) + str(h))
        return [a,h]

    def A2decry(self,cipher,key):
        a_square = int(key)
        c = int(cipher)
        const = Decimal(2 * (1 + Decimal(2).sqrt()))
        denominator = Decimal(const * a_square)
        h = Decimal(Decimal(c) / Decimal(denominator)).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        d = Decimal(a_square)
        a = Decimal(d.sqrt()).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        ascii = str(str(a) + str(h))
        return [a,h]

    def Hdecry(self,cipher,key):
        h = int(key)
        c = int(cipher)
        const = Decimal(2 * (1 + Decimal(2).sqrt()))
        denominator = Decimal(const * h)
        a_square = Decimal(Decimal(c) / Decimal(denominator)).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        d = Decimal(a_square)
        a = Decimal(d.sqrt()).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        ascii = str(str(a) + str(h))
        return [a,h]