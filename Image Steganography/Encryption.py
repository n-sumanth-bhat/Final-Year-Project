from PIL import Image


class StegoEncryption:
    def __init__(self):
        self.data = ""

    def encode(self,img,data):
        self.data = data
        self.image = Image.open(img, 'r')
        self.newimg = self.image.copy()
        self.encode_enc()
        # new_img_name = input("Enter the name of new image(with extension) : ")
        # newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))
        # print("Image saved!")

    def encode_enc(self):
        w = self.newimg.size[0]  # w is width
        (x, y) = (0, 0)
        for pixel in self.modPix():
            # Putting modified pixels in the new image
            self.newimg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1

    def modPix(self):
        datalist = self.genData()
        lendata = len(datalist)
        imdata = iter(self.newimg.getdata())
        for i in range(lendata):
            # Extracting 3 pixels at a time
            pix = [value for value in imdata.__next__()[:3] +
                   imdata.__next__()[:3] +
                   imdata.__next__()[:3]]

            # Pixel value should be made
            # odd for 1 and even for 0
            for j in range(0, 8):
                if (datalist[i][j] == '0' and pix[j] % 2 != 0):
                    pix[j] -= 1

                elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                    if (pix[j] != 0):
                        pix[j] -= 1
                    else:
                        pix[j] += 1
                # pix[j] -= 1
            # Eighth pixel of every set tells
            # whether to stop or read further.
            # 0 means keep reading; 1 means the
            # message is over.
            if (i == lendata - 1):
                if (pix[-1] % 2 == 0):
                    if (pix[-1] != 0):
                        pix[-1] -= 1
                    else:
                        pix[-1] += 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]


    # Convert encoding data into 8-bit binary
    # form using ASCII value of characters

    def genData(self):
        # list of binary codes
        # of given data
        newd = []
        for i in self.data:
            newd.append(format(ord(i), '08b'))
        return newd
