# Python program implementing Image Steganography

# PIL module is used to extract
# pixels of image and modify it
import time
from PIL import Image

# Convert encoding data into 8-bit binary
# form using ASCII value of characters
def genData(data):

		# list of binary codes
		# of given data
		newd = []

		for i in data:
			newd.append(format(ord(i), '08b'))
		return newd

# Pixels are modified according to the
# 8-bit binary data and finally returned
def modPix(pix, data):

	datalist = genData(data)
	lendata = len(datalist)
	imdata = iter(pix)

	for i in range(lendata):

		# Extracting 3 pixels at a time
		pix = [value for value in imdata.__next__()[:3] +
								imdata.__next__()[:3] +
								imdata.__next__()[:3]]

		# Pixel value should be made
		# odd for 1 and even for 0
		for j in range(0, 8):
			if (datalist[i][j] == '0' and pix[j]% 2 != 0):
				pix[j] -= 1

			elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
				if(pix[j] != 0):
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
				if(pix[-1] != 0):
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

def encode_enc(newimg, data):
	
	w = newimg.size[0] #w is width
	(x, y) = (0, 0)

	for pixel in modPix(newimg.getdata(), data):
		
		# Putting modified pixels in the new image
		newimg.putpixel((x, y), pixel)
		if (x == w - 1):
			x = 0
			y += 1
		else:
			x += 1
	
# Encode data into image
def encode():
	img = input("Enter image name(with extension) : ")
	start_time=time.time()
	image = Image.open(img, 'r')
    
	f=open("data.txt","r")
	data=f.read()
	print(len(data))
	# data=""
	# res=""
	# for x in range(99999):
	# 	res=res+(str(x))
	# print(len(data))
	# data=res
	if (len(data) == 0):
		raise ValueError('Data is empty')

	newimg = image.copy()
	encode_enc(newimg, data)

	print("len of data ",len(data))#length of data used.
	print(" Encryption Time --- %s seconds ---" % (time.time() - start_time))	
	new_img_name = input("Enter the name of new image(with extension) : ")
	newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))
	# print("--- %s seconds ---" % (time.time() - start_time))
	print("Image saved!")
# Decode the data in the image
def decode():
	img = input("Enter image name(with extension) : ")
	image = Image.open(img, 'r')
	decrypt_time=time.time()
	data = ''
	imgdata = iter(image.getdata())

	while (True):
		pixels = [value for value in imgdata.__next__()[:3] +
								imgdata.__next__()[:3] +
								imgdata.__next__()[:3]]

		# string of binary data
		binstr = ''

		for i in pixels[:8]:
			if (i % 2 == 0):
				binstr += '0'
			else:
				binstr += '1'

		data += chr(int(binstr, 2))
		if (pixels[-1] % 2 != 0):
			return data,decrypt_time
# Main Function
def main():
	a = int(input(":: Welcome to Steganography ::\n"
						"1. Encode\n2. Decode\n"))
	if (a == 1):
		encode()

	elif (a == 2):
		decrypteddata,decrypt_time=decode()
		try:
			f=open("data.txt","w")
		except:
			print("error file already exists")
		opfile=open("decrypted.txt","x")
		opfile.write(decrypteddata)
		print( " Decryption time: --- %s seconds ---" % (time.time() - decrypt_time))

		#print("Decoded Word : " + decrypteddata)
		print("Decrypted data is stored in decrypted.txt file")
	else:
		raise Exception("Enter correct input")

# Driver Code
if __name__ == '__main__' :

	# Calling main function
	main()
