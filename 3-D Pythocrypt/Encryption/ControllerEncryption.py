import random
from Encryption.HexaPrism import HexaPrismEncryption
from Encryption.OctaPrism import OctaPrismEncryption
from Encryption.Octahedron import OctahedronEncryption
from Encryption.PentaPrism import PentaPrismEncryption
from Encryption.PentaPyramid import PentaPyramidEncryption


class Controller:
    def __init__(self):
        self.plain_text = ""
        self.zero_flag = False
        self.cipher = ""
        self.s1 = ""
        self.s2 = ""
        self.equivalent_ascii = ""
        self.key = ""

    def main(self):
        print("----This is the Encryption Phase---")
        print("Enter the plain text:")
        self.plain_text = str(input())
        self.n = len(self.plain_text)
        print("Length of the plain text given is : ", self.n)
        for i in range(0, self.n):
            self.each = str(ord(self.plain_text[i]))
            self.equivalent_ascii += self.each
        print("Ascii value at encryption is ",self.equivalent_ascii)
        self.len_of_ascii = len(self.equivalent_ascii)
        self.split = self.len_of_ascii / 2
        for i in range(self.len_of_ascii):
            if i < self.split:
                self.s1 += self.equivalent_ascii[i]
            elif i >= self.split and i < self.len_of_ascii:
                self.s2 += self.equivalent_ascii[i]

        if self.s2[0] == '0':
            self.zero_flag = True
        self.identification_of_algorithm()
        self.identification_of_key()
        self.cipher = str(str(self.which_algorithm) + str(self.which_key) + str(self.cipher))
        return [self.cipher,self.key, self.zero_flag]

    def identification_of_algorithm(self):
        self.which_algorithm = random.randint(1,5)
        if self.which_algorithm == 1:
            octa = OctahedronEncryption()
            self.cipher = octa.encry(self.s1,self.s2)
        elif self.which_algorithm == 2:
            hexa = HexaPrismEncryption()
            self.cipher = hexa.encry(self.s1,self.s2)
        elif self.which_algorithm == 3:
            penta = PentaPrismEncryption()
            self.cipher = penta.encry(self.s1,self.s2)
        elif self.which_algorithm == 4:
            oprism = OctaPrismEncryption()
            self.cipher = oprism.encry(self.s1,self.s2)
        elif self.which_algorithm == 5:
            pprism = PentaPyramidEncryption()
            self.cipher = pprism.encry(self.s1,self.s2)


    def identification_of_key(self):
        self.which_key = random.randint(1,3)
        if self.which_key == 1:
            self.key = str(self.s1)
        elif self.which_key == 2:
            a_square = str(int(self.s1) * int(self.s1))
            self.key = str(a_square)
        else:
            self.key = str(self.s2)
