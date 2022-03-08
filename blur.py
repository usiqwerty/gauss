#!/usr/bin/env python3

#filter
r=2
f=[]
sigma=3
amp=1

t=[
[1,0,1,0,1],
[1,1,1,1,1],
[0,0,1,0,0],
[1,1,0,1,0],
[1,1,1,1,1]
]

#image
height=16
width=16
image=[]

def mean(a ,b):
	wid=len(a[0])
	hei=len(a)
	c=0
	sum=0
	for i in range(hei):
		for j in range(wid):
			sum+=a[i][j]*b[i][j]
			c+=1
	return sum/c

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

print("filter matrix:")
for y in range(2*r+1):
	for x in range(2*r+1):
		f[y][x]=g(x, y, r ,r, sigma, amp)

		print(round(f[y][x], 2), end='\t')
	print("")

print("Gauss blur by usiqwerty v1.0")


#image
for y in range(height):
	image.append([0]*width)
	print([0.5]*width)
###


print(mean(f,t))
