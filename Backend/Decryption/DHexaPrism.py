from decimal import *
from math import *

class HexaPrismDecryption:
    def Adecry(self,cipher, key):
        a = int(key)
        c = int(cipher)
        a_square = (a * a)
        numerator = Decimal(2 * c)
        d = Decimal(3)
        denominator = Decimal(3 * d.sqrt() * a_square)
        h = Decimal(Decimal(numerator) / Decimal(denominator)).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        ascii = str(str(key) + str(h))
        return [a,h]

    def A2decry(self,cipher,key):
        a_square = int(key)
        c = int(cipher)
        numerator = Decimal(2 * c)
        d = Decimal(3)
        denominator = Decimal(3 * d.sqrt() * a_square)
        h = Decimal(Decimal(numerator) / Decimal(denominator)).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        d = Decimal(key)
        a = Decimal(d.sqrt()).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        ascii = str(str(a) + str(h))
        return [a,h]

    def Hdecry(self,cipher,key):
        h = int(key)
        c = int(cipher)
        numerator = Decimal(2 * c)
        d = Decimal(3)

        denominator = Decimal(3 * d.sqrt() * h)
        a_square = Decimal(Decimal(numerator) / Decimal(denominator)).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        d = Decimal(a_square)
        a = Decimal(d.sqrt()).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        ascii = str(str(a) + str(h))
        return [a,h]



