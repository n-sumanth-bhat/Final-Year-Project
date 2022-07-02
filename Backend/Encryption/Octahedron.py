from decimal import *
getcontext().prec = 100000
getcontext().rounding = ROUND_HALF_DOWN

class OctahedronEncryption:
    def encry(self,s1,s2):
        b1 = int(s1)
        h1 = int(s2)
        b2 = (b1 * b1)
        numerator = (h1 * 2 * b2)
        cipher = (Decimal(numerator) / Decimal(3)).quantize(Decimal(1.00), ROUND_HALF_DOWN)

        print()
        str_cipher = str(cipher)
        return str_cipher
