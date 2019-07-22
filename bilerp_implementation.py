#bilinear interpolation between four points with dark/light values entailed in points matrix
from PIL import Image, ImageDraw
import sys,random,numpy
#image dimensions and point lightness values
image_width=200 
image_height=600
points = [[30,0],[255,255]]
noise = Image.new('RGBA', [image_width, image_height], (255,255,255,200))
draw_noise = ImageDraw.Draw(noise)
#slope between top two points and slope between bottom two points 
hor_slopes = [(points[0][1]-points[0][0])/image_width,(points[1][1]-points[1][0])/image_height]
for x in range(0,image_width):
    for y in range(0,image_height):
        interp_val = int((hor_slopes[0]*x+points[0][0]) + (-hor_slopes[0]*x-points[0][0]+hor_slopes[1]*x+points[1][0])/image_height*y)
        draw_noise.point([x,y], (interp_val,interp_val,interp_val,255))
#draws on the image in a light purple the light/dark values used
draw_noise.text((10,10), "values used:" + str(points) , fill=(180,130,235,208))
del draw_noise
noise.save(str(points),format="PNG")
noise.show()