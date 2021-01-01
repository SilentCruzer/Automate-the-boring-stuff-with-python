import os
from PIL import Image

square_fit_size = 300
logo = 'catlogo.png'

logoIm = Image.open(logo)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)

for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg') or filename.endswith('.gif')or filename.endswith('.bpm')) or filename == logo:
        continue
    im = Image.open(filename)
    width, height = im.size
    if width > square_fit_size and height > square_fit_size:
        if width > height:
            height = int((square_fit_size / width) * height)
            width = square_fit_size
        else:
            width = int((square_fit_size / height) * width)
            height = square_fit_size

        width, height = im.size

        if width > logoWidth*2 and height > logoHeight*2 :
            im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
            im.save(os.path.join('withLogo', filename))
        else:
            print("Image is too small")