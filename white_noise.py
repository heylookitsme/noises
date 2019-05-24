#woooo
from PIL import ImageDraw, Image
import sys,random

#sys params
image_width = int(sys.argv[1])
image_length = int(sys.argv[2])

#making image
im = Image.new('RGBA', [image_width, image_length], (255,255,255,200))
draw = ImageDraw.Draw(im)

#gen noise
noise = [random.randint(0,255) for x in range(0,image_width * image_length)]
for x in range(0,image_width):
	for y in range(0,image_length):
		draw.point([x,y],(noise[x + y*(image_width-1)],noise[x + y*(image_width-1)],noise[x + y*(image_width-1)],255))

del draw

#show
im.show()
