from Backend.Decryption.DHexaPrism import HexaPrismDecryption
from Backend.Decryption.DOctaPrism import OctaPrismDecryption
from Backend.Decryption.DOctahedron import OctahedronDecryption
from Backend.Decryption.DPentaPrism import PentaPrismDecryption
from Backend.Decryption.DPentaPyramid import PentaPyramidDecryption
from Backend.Decryption.Steganography_Decryption import StegoDecryption
from Backend.Encryption.progress import progress_bar,remove_progress_bar
from Backend.Decryption.PrintMessage import print_error_message
import time


class DController:
    def __init__(self):
        self.cipher = ""
        self.key = ""
        self.zero_flag = False
        self.ascii = []

    def main(self,data):
        self.cipher = data[0][2:]
        self.key = data[1]
        self.zero_flag = data[2]
        self.algorithm = data[0][0]
        self.key_type = data[0][1]
        self.obj = None
        for i in range(35,45):
            time.sleep(.008)
            progress_bar(i)
        self.specific_algorithm_object()
        for i in range(45,60):
            time.sleep(.008)
            progress_bar(i)
        self.extracting_ascii()
        for i in range(60,80):
            time.sleep(.008)
            progress_bar(i)
        self.s1 = self.ascii[0]
        self.s2 = self.ascii[1]

        self.plain_text_extraction()
        for i in range(80,95):
            time.sleep(.008)
            progress_bar(i)
        return

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

    def Image_steganography(self,img):
        progress_bar(0)
        imgste = StegoDecryption()
        text = imgste.decode(img)
        if not text.isprintable():
            remove_progress_bar()
            print_error_message("Given image is not a stego-Image(file)!","Error",0)
            exit()
        for i in range(1,25):
            time.sleep(.008)
            progress_bar(i)
        data = text.split('.')
        key = data[1]
        zero_flag = int(key[-1])
        data.remove(data[1])
        data.append(key[:-1])
        data.append(bool(zero_flag))
        for i in range(25,35):
            time.sleep(.008)
            progress_bar(i)
        self.main(data)
        return (1,len(text),int(self.algorithm),self.message)



