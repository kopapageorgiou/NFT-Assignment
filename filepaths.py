import os

main_path = os.getcwd() + "/substrapunks-master/scripts/face_parts/"
path_prefix = {
    "face": main_path + "face/",
    "ears": main_path + "ears/",
    "eyes": main_path + "eyes/",
    "hair": main_path + "hair/",
    "mouth" : main_path + "mouth/",
    "nose" : main_path + "nose/"
}

face_files = {
    "White": path_prefix["face"] + "face1.png",
    "Black": path_prefix["face"] + "face2.png"
}

ears_files = {
    "No Earring": path_prefix["ears"] + "ears1.png",
    "Left Earring": path_prefix["ears"] + "ears2.png",
    "Right Earring": path_prefix["ears"] + "ears3.png",
    "Two Earrings": path_prefix["ears"] + "ears4.png"
}

eyes_files = {
    "Regular": path_prefix["eyes"] + "eyes1.png",
    "Small": path_prefix["eyes"] + "eyes2.png",
    "Rayban": path_prefix["eyes"] + "eyes3.png",
    "Hipster": path_prefix["eyes"] + "eyes4.png",
    "Focused": path_prefix["eyes"] + "eyes5.png"     
}

hair_files = {
    "Up Hair": path_prefix["hair"] + "hair1.png",
    "Down Hair": path_prefix["hair"] + "hair2.png",
    "Mohawk": path_prefix["hair"] + "hair3.png",
    "Red Mohawk": path_prefix["hair"] + "hair4.png",
    "Orange Hair": path_prefix["hair"] + "hair5.png",
    "Bubble Hair": path_prefix["hair"] + "hair6.png",
    "Emo Hair": path_prefix["hair"] + "hair7.png",
    "Thin Hair": path_prefix["hair"] + "hair8.png",
    "Bald": path_prefix["hair"] + "hair9.png",
    "Blonde Hair": path_prefix["hair"] + "hair10.png",
    "Caret Hair": path_prefix["hair"] + "hair11.png",
    "Pony Tails": path_prefix["hair"] + "hair12.png"
}


mouth_files = {
    "Black Lipstick": path_prefix["mouth"] + "m1.png",
    "Red Lipstick": path_prefix["mouth"] + "m2.png",
    "Big Smile": path_prefix["mouth"] + "m3.png",
    "Smile": path_prefix["mouth"] + "m4.png",
    "Teeth Smile": path_prefix["mouth"] + "m5.png",
    "Purple Lipstick": path_prefix["mouth"] + "m6.png"
}

nose_files = {
    "Nose": path_prefix["nose"] + "n1.png",
    "Nose Ring": path_prefix["nose"] + "n2.png"   
}