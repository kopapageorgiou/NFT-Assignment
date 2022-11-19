from PIL import Image
from IPython.display import display
import random, string
import json
import os
import rarity as rar
import filepaths as fl
import ipfsApi
from BlockchainLib import *
from generate_metadata import *
from brownie import accounts
from web3.auto import w3
from eth_account.messages import encode_defunct
from eth_utils import keccak
from eth_abi.packed import encode_abi_packed
from io import BytesIO
import requests
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

    img1 = Image.open(fl.face_files[image["face"]]).convert('RGBA')
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

    return com5

image = create_new_image()

if not os.path.exists("./images"):
    os.mkdir(f'./images')

letters = string.ascii_uppercase

rgb_im = generate_image(image).convert('RGB')
file_name = ''.join(random.choice(letters) for i in range(10))
rgb_im.save("./images/" + file_name +".png")
api = ipfsApi.Client('127.0.0.1', 5001)
smartContract = smartContract('settings.ini')
#smartContract.transferEther(20, "0x1d939efF66e4120C69434e89a95C19c0d4FE21c7")
res = api.add(f'./images/{file_name}.png')
print(res)
url = f"http://ipfs.io/ipfs/{res[0]['Hash']}?filename={file_name}.png"
image['external_link'] = url
fullname = input("Your Name: ")
image['tokenId'] = smartContract.getCurrentId()
createMetadata(image, file_name+".json")
metadata = json.dumps(image, indent=4)
res = api.add(f'./metadata/{file_name}.json')
account = accounts.load('papas')

print(metadata)
mes = smartContract.getEthHash(metadata)
print(mes)
signature = w3.eth.account.signHash(mes, account.private_key)
print(signature)
print(str(signature.signature))
tx = smartContract.mint(account.address, signature.signature, fullname, metadata)
print(tx)
tx1 = smartContract.getNFT(smartContract.getCurrentId())
print(tx1)
metadata = json.loads(tx1[0])
print(metadata)
file_name = metadata['external_link'].split('=')[-1]
response = requests.get(metadata['external_link'])

img = Image.open(BytesIO(response.content))
img.show()