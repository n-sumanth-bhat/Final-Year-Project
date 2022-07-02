from DHexaPrism import HexaPrismDecryption
from DOctaPrism import OctaPrismDecryption
from DOctahedron import OctahedronDecryption
from DPentaPrism import PentaPrismDecryption
from DPentaPyramid import PentaPyramidDecryption

class DController:
    def __init__(self):
        self.cipher = ""
        self.key = ""
        self.zero_flag = False
        self.ascii = []

    def main(self,data):
        print("The Cipher text is:")
        print(data[0])
        print()
        print("Key is:")
        print(data[1])
        print()
        self.cipher = data[0][2:]
        self.key = data[1]
        self.zero_flag = data[2]
        self.algorithm = data[0][0]
        self.key_type = data[0][1]
        self.obj = None

        self.specific_algorithm_object()
        self.extracting_ascii()

        self.s1 = self.ascii[0]
        self.s2 = self.ascii[1]

        self.plain_text_extraction()
        return(self.message)

    def specific_algorithm_object(self):
        if self.algorithm == "1":
            self.obj = OctahedronDecryption()
        elif self.algorithm == "2":
            self.obj = HexaPrismDecryption()
        elif self.algorithm == "3":
            self.obj = PentaPrismDecryption()
        elif self.algorithm == "4":
            self.obj = OctaPrismDecryption()
        else:
            self.obj = PentaPyramidDecryption()


    def extracting_ascii(self):
        if self.key_type == "1":
            self.ascii = self.obj.Adecry(self.cipher,self.key)
        elif self.key_type == "2":
            self.ascii = self.obj.A2decry(self.cipher,self.key)
        else:
            self.ascii = self.obj.Hdecry(self.cipher,self.key)


    def plain_text_extraction(self):
        if self.zero_flag:
            self.s2 = '0' + str(self.s2)

        self.equivalent_ascii = str(str(self.s1) + str(self.s2))
        self.message = ""
        num = int(0)
        for i in range(0, len(self.equivalent_ascii)):
            num = num * 10 + (ord(self.equivalent_ascii[i]) - ord('0'))
            if num >= 32 and num <= 122:
                ch = chr(num)
                self.message += ch
                num = 0
        print()


