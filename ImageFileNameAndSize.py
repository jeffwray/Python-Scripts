from PIL import Image
import os

# Use the current working directory
ios_splash_screens_folder = os.getcwd()

# Iterate through the files in the folder
for filename in os.listdir(ios_splash_screens_folder):
    if filename.endswith(".png"):
        file_path = os.path.join(ios_splash_screens_folder, filename)
        image = Image.open(file_path)
        width, height = image.size
        print(f'{{"ios", "{filename}", {width}, {height}}},')


