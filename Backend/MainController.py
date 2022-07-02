import sys

from py import process
from Backend.Decryption.ControllerDecryption import DController
from Backend.Encryption import ControllerEncryption
from Backend.Encryption.progress import progress_bar
import os
import time
from time import process_time

def encryption(plain_text):
        encry = ControllerEncryption.Controller()
        en_start = process_time()
        status,cipher_length,which_algorithm,image = encry.main(plain_text)
        en_stop = process_time()
        if status != 1:
            return ("fail",None,None,None)
        else:
            for i in range(85,101):
                time.sleep(.008)
                progress_bar(i)
            print()
            elapsed_time = en_stop - en_start
            return ("success",cipher_length,which_algorithm,image,elapsed_time)
    
def decryption(path):
        decry = DController()
        de_start = process_time()
        status,cipher_length,which_algorithm,message = decry.Image_steganography(path)
        de_stop = process_time()
        elapsed_time = de_stop - de_start
        if status != 1:
            return("fail",None,None,None)
        else:
            for i in range(95,101):
                time.sleep(.008)
                progress_bar(i)
            print()
            return ("success",cipher_length,which_algorithm,message,elapsed_time)

