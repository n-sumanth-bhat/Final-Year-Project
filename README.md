
# Enigma - A Tool For Cybersecurity

- This is a cryptography project. We designed and developed the new cryptographic algorithm called 3D Pythocypt algorithm. This is a young technique where key is used only at the decryption phase. 
- The ideology of 3D Pythocrypt is to encrypt the plain text using the properties of 3D geometric shapes.
- We have considered volumetric formula of five different geometric shapes in this project.
- To securely transmit the cipher text obtained from the 3D pythocrypt algorithm, the cipher text is hidden inside the pixels of the image using LSB algorithm in Image Steganography.



## Why Enigma?

- Although there are many Symmetric and Asymmetric Cryptographic systems available, a new cryptgraphic system is necessary in this social world.
- If we want to transmit huge amount of data from sender to receiver, then we can use Enigma as a stand alone application or as an api.
- The estimated amount of data that the algorithm takes as an input at a given time is around 2^(2147483647) that is approximately 646456993 characters.
- Subsequently, as we have used five different shapes, there are three possible key values for each shape. Hence, there are 15 possible combinations that can be achieved. This makes the algorithm more secure.
- Eventhough the operations to be performed are more, the time complexity of the 3D Pythocrypt algorithm is efficient than most of the current cryptosystems.

## Tech Stack

- Programming Language:
    - Python
        - Click
        - pyInquirer
        - rich
        - Colorama and other inbuilt python libraries


## Authors

- [@Sumanth N](https://github.com/n-sumanth-bhat)
- [@Shrinidhi Holla](https://github.com/Shrinidhi-Holla)


## How to Execute?

- Download the zip file to a directory and unzip the same or clone the repository
- Walk through the folder structure till you find "Enigma.py" file
- Open the directory in the command prompt
- Give "enigma" command to launch the application.
- If you face any error, then install the following packages
- pip install click
- pip install pyInquirer
- pip install rich


## Features

- CLI Interface
- Custom Progress Bar
- Implementing Custom Commands
- Cross platform


## API Reference

- [Click](https://click.palletsprojects.com/en/8.1.x/)
- [Colorama](https://pypi.org/project/colorama/)
- [Rich](https://rich.readthedocs.io/en/stable/introduction.html)

## Screenshots

- Downloading the Project
![App Screenshot](https://github.com/n-sumanth-bhat/Final-Year-Project/blob/main/Screenshots/Downloading%20the%20Project.PNG)

- Launching the Application
![App Screenshot](https://github.com/n-sumanth-bhat/Final-Year-Project/blob/main/Screenshots/Launching%20the%20application.PNG)

- Help (--help) command
![App Screenshot](https://github.com/n-sumanth-bhat/Final-Year-Project/blob/main/Screenshots/help%20command.PNG)

- encrypt command
![App Screenshot](https://github.com/n-sumanth-bhat/Final-Year-Project/blob/main/Screenshots/encrypt%20command.PNG)

- decrypt command
![App Screenshot](https://github.com/n-sumanth-bhat/Final-Year-Project/blob/main/Screenshots/decrypt%20command.PNG)

- performance stats
![App Screenshot](https://github.com/n-sumanth-bhat/Final-Year-Project/blob/main/Screenshots/info%20about%20previous%20operation.PNG)

- Error
![App Screenshot](https://github.com/n-sumanth-bhat/Final-Year-Project/blob/main/Screenshots/not%20a%20stego%20image.PNG)


## Acknowledgements

We would like to thank and dedicate this project to all the instructors who are in various platform guiding and helping the students to achieve their goal.



## Future Work

- The present version takes the raw plaintext from the command line, an option can be provided for the user to input the plaintext from a .txt file
- Furthermore, the application can be made robust which can encrypt any file formats such as .pdf, .doc, .xls etc.

## Feedback

If you have any feedback or queries, please reach out to
- [Sumanth N](mailto:nsumanthbhat@gmail.com)

