from PIL import Image
from IPython.display import display
import random
import json
import os
import rarity as rar
import filepaths as fl
TOTAL = 1

all_images = []

def create_new_image():
    new_image = {}

    new_image["face"] = random.choices(rar.face, rar.face_weights)[0]
    new_image["ears"] = random.choices(rar.ears, rar.ears_weights)[0]
    new_image["eyes"] = random.choices(rar.eyes, rar.eyes_weights)[0]
    new_image["hair"] = random.choices(rar.hair, rar.hair_weights)[0]
    new_image["mouth"] = random.choices(rar.mouth, rar.mouth_weights)[0]
    new_image["nose"] = random.choices(rar.nose, rar.nose_weights)[0]

    if new_image in all_images:
        return create_new_image()
    else:
        return new_image

for i in range(TOTAL):
    all_images.append(create_new_image())

def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))
# Add token Id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1
   
print(all_images)

face_count = {}
for item in rar.face:
    face_count[item] = 0
    
ears_count = {}
for item in rar.ears:
    ears_count[item] = 0

eyes_count = {}
for item in rar.eyes:
    eyes_count[item] = 0
    
hair_count = {}
for item in rar.hair:
    hair_count[item] = 0
    
mouth_count = {}
for item in rar.mouth:
    mouth_count[item] = 0
    
nose_count = {}
for item in rar.nose:
    nose_count[item] = 0

for image in all_images:
    face_count[image["face"]] += 1
    ears_count[image["ears"]] += 1
    eyes_count[image["eyes"]] += 1
    hair_count[image["hair"]] += 1
    mouth_count[image["mouth"]] += 1
    nose_count[image["nose"]] += 1
    
print(face_count)
print(ears_count)
print(eyes_count)
print(hair_count)
print(mouth_count)
print(nose_count)
if not os.path.exists("./images"):
    os.mkdir(f'./images')

for item in all_images:
    img1 = Image.open(fl.face_files[item["face"]]).convert('RGBA')
    img2 = Image.open(fl.eyes_files[item["eyes"]]).convert('RGBA')
    img3 = Image.open(fl.ears_files[item["ears"]]).convert('RGBA')
    img4 = Image.open(fl.hair_files[item["hair"]]).convert('RGBA')
    img5 = Image.open(fl.mouth_files[item["mouth"]]).convert('RGBA')
    img6 = Image.open(fl.nose_files[item["nose"]]).convert('RGBA')

    com1 = Image.alpha_composite(img1, img2)
    com2 = Image.alpha_composite(com1, img3)
    com3 = Image.alpha_composite(com2, img4)
    com4 = Image.alpha_composite(com3, img5)
    com5 = Image.alpha_composite(com4, img6)

    rgb_im = com5.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)
