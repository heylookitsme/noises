#todo: learn how to use iterators before I blow my brains out
from PIL import Image, ImageDraw
import sys,random,numpy
image_width=300 
image_height=400
points_hor=9
points_ver=9
block_width=image_width/(points_hor-1)
block_height=image_height/(points_ver-1)

points = numpy.random.randint(256, size=(points_ver,points_hor))
print(points)
points_slopes = numpy.zeros((points_ver-1,points_hor-1))
for y in range(0,points_ver-1):
    for x in range(0,points_hor-1): 
        points_slopes[y][x] = (points[y][x+1]-points[y][x])/block_width
interp_vals = numpy.zeros((image_height,image_width))
vert_slp = numpy.zeros((points_ver-1,image_width))
for x in range(0,image_width):
    for y in range(0,image_height):
            slope = vert_slp[int(y/block_height)][x]
            interp_vals[y][x] = int((x%block_width)*points_slopes[int(y/block_height)][int(x/block_width)]+points[int(y/block_height)][int(x/block_width)]+slope*(y%block_height))
for x in range(0,image_width):
    for y in range(0,points_ver-2):
        kill=interp_vals[int(block_height+(y*block_height))][x]-interp_vals[int((y*block_height))][x]
        vert_slp[y][x]=kill/block_height
for x in range(0,image_width):
    for y in range(0,image_height):
            slope = vert_slp[int(y/block_height)][x]
            interp_vals[y][x] = int((x%block_width)*points_slopes[int(y/block_height)][int(x/block_width)]+points[int(y/block_height)][int(x/block_width)]+slope*(y%block_height))
noise = Image.new('RGBA', [image_width, image_height], (255,255,255,200))
draw_noise = ImageDraw.Draw(noise)
for x in range(0,image_width):
    for y in range(0,image_height):
        draw_noise.point([x,y],(int(interp_vals[y][x]),int(interp_vals[y][x]),int(interp_vals[y][x]),255))
        
del draw_noise
noise.save( "9x9"+ "value noise",format="PNG")
noise.show()