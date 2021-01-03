from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

def custom(guest):
	card = Image.new('RGBA', (280,352), 'red')
	img = Image.open('flower.png')
	card.paste(img,(10,0),img)
	border = Image.new('RGBA',(288,360), 'black')
	border.paste(card,(4,3))
	draw = ImageDraw.Draw(border)
	font = ImageFont.truetype('Purisa-Bold.ttf', 30)
	draw.text((50,290), guest, fill='black',font=font)
	filename = guest + '_card.png'
	border.save(filename)

with open("guests.txt") as file:
	guests_list = file.readlines()
	guests_list = [line.strip() for line in guests_list]

for name in guests_list:
	custom(name)

