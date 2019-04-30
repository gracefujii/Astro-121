import numpy as np
import matplotlib.pyplot as plt
import pyfits

fits = pyfits.open('data_apr19_126.520972417_59.9346594914.fits')
fits1 = pyfits.open('data_apr19_126.894036433_61.5627697823.fits')
fits2 = pyfits.open('data_apr19_127.380501724_63.185455425.fits')

print fits[0].header.keys()
print fits[0].header['TIME']
print fits[0].header['L']
print fits[0].header['B']
print fits[0].header['NAXIS']
print fits[0].header['RA']
print fits[0].header['DEC']

a = 0
b = 0
c = 0
lst = []
lst1 = []
lst2 = []
lst3 = []

while a < 8190:
	lst.append(fits[1].data[a][0])
	a += 1
while b < 8190:
	lst1.append(fits1[1].data[b][0])
	b += 1
while c < 8190:
	lst2.append(fits2[1].data[c][0])
	c += 1


plt.plot(lst)
plt.plot(lst1)
plt.plot(lst2)
plt.show()


