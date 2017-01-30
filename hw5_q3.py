from PIL import Image
import math
import numpy as np
from scipy.misc import toimage

def kMean(pix,k):
	#sort pixel values
	pixList=[]
	for i in range(1024):
		for j in range(768):
			pixList.append(pix[i][j])
	pixList.sort()

	#initialize k-means
	a=int(math.floor(float(len(pixList))/k))
	mean=[]
	for i in range(k):
		mean.append(pixList[(i+1)*a-1])

	#classify pixel values to k-groups
	pixGroup=[[0 for x in range(768)] for y in range(1024)] 
	for i in range(1024):
		for j in range(768):
			g=0
			for m in range(len(mean)):
				if( abs(pix[i][j]-mean[m]) < abs(pix[i][j]-mean[g]) ):
					g=m
			pixGroup[i][j]=g

	#Update k-means
	a=[0]*k
	b=[0]*k
	for i in range(1024):
		for j in range(768):
			a[pixGroup[i][j]]+=pix[i][j]
			b[pixGroup[i][j]]+=1

	newMean=[0]*k
	for i in range(k):
		newMean[i]=int(float(a[i])/b[i])

	#difference between old k-mean and new k-mean
	diff=0
	for i in range(k):
		if(mean[i] != newMean[i]):
			diff=1
			break

	while(diff==1):
		mean=newMean

		#classify pixel values to k-groups
		pixGroup=[[0 for x in range(768)] for y in range(1024)] 
		for i in range(1024):
			for j in range(768):
				g=0
				for m in range(len(mean)):
					if( abs(pix[i][j]-mean[m]) < abs(pix[i][j]-mean[g]) ):
						g=m
				pixGroup[i][j]=g

		#Update k-means
		a=[0]*k
		b=[0]*k
		for i in range(1024):
			for j in range(768):
				a[pixGroup[i][j]]+=pix[i][j]
				b[pixGroup[i][j]]+=1

		newMean=[0]*k
		for i in range(k):
			newMean[i]=int(float(a[i])/b[i])

		#difference between old k-means and new k-means
		diff=0
		for i in range(k):
			if(mean[i] != newMean[i]):
				diff=1
				break

	#regularization
	for i in range(1024):
			for j in range(768):
				pix[i][j]=mean[pixGroup[i][j]]

	return (pix,pixGroup,mean)

#decide value of k
k=4
im = Image.open('raccoon.png').convert("L")
pixel = im.load()

pix=[]
for i in range(1024):
	a=[]
	for j in range(768):
		a.append(pixel[i,j])
	pix.append(a)

#group is the 2D-matrix of group assignments for each pixel,mean is the mean value for each group
(newPixel,group,mean)=kMean(pix,k)

print "mean of group 1 is "+str(mean[0])
print "mean of group 2 is "+str(mean[1])
print "mean of group 3 is "+str(mean[2])
print "mean of group 4 is "+str(mean[3])

newPix=np.array(newPixel)
newPix_trans=np.transpose(newPix)
toimage(newPix_trans).save("k=15.png")
toimage(newPix_trans).show()
