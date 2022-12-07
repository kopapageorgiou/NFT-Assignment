from PIL import Image
import random, string
import os
import rarity as rar
import filepaths as fl
#import ipfsapi #!Deprecated
from BlockchainLib import *
from generate_metadata import *
import platform
image = {}

def create_new_image():
    new_image = {}
    new_image["face"] = random.choices(rar.face, rar.face_weights)[0]
    new_image["ears"] = random.choices(rar.ears, rar.ears_weights)[0]
    new_image["eyes"] = random.choices(rar.eyes, rar.eyes_weights)[0]
    new_image["hair"] = random.choices(rar.hair, rar.hair_weights)[0]
    new_image["mouth"] = random.choices(rar.mouth, rar.mouth_weights)[0]
    new_image["nose"] = random.choices(rar.nose, rar.nose_weights)[0]

    return new_image

def generate_image(image):

    img1 = Image.open(fl.face_files[image["face"]]).convert('RGBA',)
    img2 = Image.open(fl.eyes_files[image["eyes"]]).convert('RGBA')
    img3 = Image.open(fl.ears_files[image["ears"]]).convert('RGBA')
    img4 = Image.open(fl.hair_files[image["hair"]]).convert('RGBA')
    img5 = Image.open(fl.mouth_files[image["mouth"]]).convert('RGBA')
    img6 = Image.open(fl.nose_files[image["nose"]]).convert('RGBA')

    com1 = Image.alpha_composite(img1, img2)
    com2 = Image.alpha_composite(com1, img3)
    com3 = Image.alpha_composite(com2, img4)
    com4 = Image.alpha_composite(com3, img5)
    com5 = Image.alpha_composite(com4, img6)
    image = Image.new("RGBA", com5.size, color="GRAY")
    image.paste(com5, mask=com5)

    if platform.system() == "Windows":
        
        if not os.path.exists(".\\images"):
            print('here')
            os.mkdir(f'.\\images')
    else:
        if not os.path.exists("./images"):
            os.mkdir(f'./images')


    rgb_im = image.convert('RGB')
    return rgb_im

def save_image(image):

    letters = string.ascii_uppercase
    file_name = ''.join(random.choice(letters) for i in range(10))
    if platform.system() == "Windows":
        image.save(".\\images\\" + file_name +".png")
    else:
        image.save("./images/" + file_name +".png")
    return file_name
