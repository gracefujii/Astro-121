from __future__ import unicode_literals
import joypy
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm
import csv
import pyfits
import seaborn as sns




fits = pyfits.open('data1.fits')

x = []
y = []

lst = []
csvData = []
def avg_spectrum(fits):
    power_1 = []
    power_2 = []
    for i in range(len(fits)-1):
        pol_1 = fits[i+1].data['auto0_real']
        pol_2 = fits[i+1].data['auto0_real']
        power_1.append(pol_1)
        power_2.append(pol_2)

    power = power_1 + power_2

    avg_power = sum(power)/len(power)
    return avg_power
plt.plot(avg_spectrum(fits))
plt.show()

i = 2
csvData = [[1, 0.006680496968328953], [2, 0.00728455837816,], [3, 0.007168341428041458], [4, 0.007449348457157612]]
while i < 100:
    csvData.append([i,fits[1].data[i][0]])
    i+=1

#print csvData
with open('person.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(csvData)

csvFile.close()

joypy.joyplot(csvData)
plt.xlabel('wavelength(cm)')
plt.show()
