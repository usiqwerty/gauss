#!/usr/bin/env python3
from PIL import Image
import numpy as np
DEBUG=False

#image
img = Image.open("file.bmp")
tmp=list(img.getdata())

height=img.height
width=img.width

image=[]
for i in range(height):
	image.append([0]*width)

for i in range(len(tmp)):
	x=i%width
	y=i//width
	image[y][x]=tmp[i]


#filter
f=[]
r=5
sigma=5//2
amp=sigma+1

img.close()

#weighted mean
def mean(mask, data, x0 ,y0):
	wid=len(mask[0])
	hei=len(mask)
	c=0
	sum=0
	for y in range(hei):
		for x in range(wid):
			if (x+x0-r)<width and (y+y0-r)<height:
				sum+=mask[y][x]*data[y+y0-r][x+x0-r]
				c+=1
	return sum/c
#gaussian function
def g(x, y, x0, y0, sig, A):
	e=2.718281828459045
	a=( (x-x0)**2 ) / (2*sig**2)
	b=( (y-y0)**2 ) / (2*sig**2)
	c=-(a+b)
	return A * (e**c)


#filter setup
for y in range(2*r+1):
	row=[]
	for x in range(2*r+1):
		row.append( g(x, y, r ,r, sigma, amp) )
	f.append(row)
#filter is ready

if DEBUG:
	print("filter matrix:")
	for y in range(2*r+1):
		for x in range(2*r+1):
			f[y][x]=g(x, y, r ,r, sigma, amp)
			print(round(f[y][x], 2), end='\t')
		print("")

print("Gauss blur by usiqwerty v1.0")


out=[]
for y in range(height):
	for x in range(width):
		out.append(int( mean(f,image, x, y) ))

new=Image.frombytes('L', (width, height), bytes(out))
new.save('out.bmp', 'BMP')
new.close()
