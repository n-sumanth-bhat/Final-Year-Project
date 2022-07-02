import random
import time
from Backend.Encryption.HexaPrism import HexaPrismEncryption
from Backend.Encryption.OctaPrism import OctaPrismEncryption
from Backend.Encryption.Octahedron import OctahedronEncryption
from Backend.Encryption.PentaPrism import PentaPrismEncryption
from Backend.Encryption.PentaPyramid import PentaPyramidEncryption
from Backend.Encryption.Steganography_Encryption import StegoEncryption
from Backend.Encryption.progress import progress_bar

class Controller:
    def __init__(self):
        
        self.plain_text = ""
        self.zero_flag = False
        self.cipher = ""
        self.s1 = ""
        self.s2 = ""
        self.equivalent_ascii = ""
        self.key = ""

    def main(self,plain_text):
        self.plain_text = plain_text
        self.n = len(self.plain_text)
        progress_bar(0)
        for i in range(0, self.n):
            self.each = str(ord(self.plain_text[i]))
            self.equivalent_ascii += self.each
        for i in range(1,10):
            time.sleep(.008)
            progress_bar(i)
        self.len_of_ascii = len(self.equivalent_ascii)
        self.split = self.len_of_ascii / 2
        for i in range(self.len_of_ascii):
            if i < self.split:
                self.s1 += self.equivalent_ascii[i]
            elif i >= self.split and i < self.len_of_ascii:
                self.s2 += self.equivalent_ascii[i]
        for i in range(10,25):
            time.sleep(.008)
            progress_bar(i)
        if self.s2[0] == '0':
            self.zero_flag = True
        for i in range(25,34):
            progress_bar(i)
        self.identification_of_algorithm()

        for i in range(34,50):
            time.sleep(.008)
            progress_bar(i)
        self.identification_of_key()
        for i in range(50,60):
            time.sleep(.008)
            progress_bar(i)
        self.cipher = str(str(self.which_algorithm) + str(self.which_key) + str(self.cipher))
        for i in range(60,70):
            time.sleep(0.007)
            progress_bar(i)
        return (1,len(self.cipher),self.which_algorithm,self.Image_Steganography())

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

    def Image_Steganography(self):
        imgste = StegoEncryption()
        self.cipher_text = str(str(self.cipher)+'.'+str(self.key)+str(int(self.zero_flag)))

        num = random.randint(1,10)
        path = ".\\Backend\\Assets\\"
        img = path+"I"+str(num)+".png"
        encrypted_img = imgste.encode(img,self.cipher_text)
        #encrypted_img.save("D:\\Sumanth\\Final year Project\\Enigma - Implementation\\output_Images\\ENCRYPTED_"+"I"+str(num)+".png")
        #print("ENCRYPTED_I"+str(num))
        #print("Image Saved Successfully!!!")
        for i in range(70,85):
            time.sleep(.008)
            progress_bar(i)
        return encrypted_img

