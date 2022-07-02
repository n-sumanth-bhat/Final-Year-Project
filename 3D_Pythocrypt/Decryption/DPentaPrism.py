from decimal import *
from math import *

class PentaPrismDecryption:
    def Adecry(self,cipher,key):
        a = int(key)
        c = int(cipher)
        const = Decimal(sqrt(5 * (5 + (2 * sqrt(5)))))
        a_square = (a * a)
        numerator = Decimal(4 * c)
        denominator = Decimal(const * a_square)
        h = Decimal(Decimal(numerator) / Decimal(denominator)).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        ascii = str(str(a) + str(h))
        return [a,h]

    def A2decry(self,cipher,key):
        a_square = int(key)
        c = int(cipher)
        const = Decimal(sqrt(5 * (5 + (2 * sqrt(5)))))
        numerator = Decimal(4 * c)
        denominator = Decimal(const * a_square)
        h = Decimal(Decimal(numerator) / Decimal(denominator)).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        d = Decimal(key)
        a = Decimal(d.sqrt()).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        ascii = str(str(a) + str(h))
        return [a,h]

    def Hdecry(self,cipher,key):
        h = int(key)
        c = int(cipher)
        const = Decimal(sqrt(5 * (5 + (2 * sqrt(5)))))
        numerator = Decimal(4 * c)
        denominator = Decimal(const * h)
        a_square = Decimal(Decimal(numerator) / Decimal(denominator)).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        d = Decimal(a_square)
        a = Decimal(d.sqrt()).quantize(Decimal(1.00), ROUND_HALF_DOWN)
        ascii = str(str(a) + str(h))
        return [a,h]

