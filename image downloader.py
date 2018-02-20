# important libaries
import random
import urllib.request

# author info
__author__ = "Francis F. Massaquoi, Jr."

# loop for the user name
while True:
    user_name = input("What is your name? ")
    if user_name.isalpha() == True:
        print("Welcome ", user_name, "this program will help you download images from the internet only .jpg images are supported")
        break
    else:
        print("Please enter your name to continue")

print("In this program, we're going to download image from the internet using python\n please paste the link below: example: https://www.google/com/image.jpg")

input("Press enter to continue")

# main function, image downloader
def image_downloader(url):
    name_generator = random.randint(1, 50)
    real_name = str(name_generator) + '.jpg'

    urllib.request.urlretrieve(url, real_name)

image_downloader(input("Paste the link here to continue: "))