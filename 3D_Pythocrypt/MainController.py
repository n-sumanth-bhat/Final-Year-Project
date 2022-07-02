from Decryption.ControllerDecryption import DController
from Encryption import ControllerEncryption

class Controller:
    encry = ControllerEncryption.Controller()
    data = encry.main()
    decry = DController()
    message = decry.main(data)
    print("Original plain text is:")
    print(message)