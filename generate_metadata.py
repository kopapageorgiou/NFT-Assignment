import json, os

if not os.path.exists(f'./metadata'):
    os.mkdir(f'./metadata')

def createMetadata(images: dict, output: str):
    if not os.path.exists(f'./metadata'):
        os.mkdir(f'./metadata')
    with open(f"./metadata/"+output, 'w') as outfile:
        json.dump(images, outfile, indent=4)
  