import os
import csv
from csv import reader
from pathlib import Path

imagedir = 'G:/NBG_NonTypes'
imageFile = 'ListScannedSpecimensOnDisk_NBG_NonTypes.csv'

def imageNames(dir):
    imageList = []
    images = os.listdir(dir)
    for image in images:
        image = Path(image).stem
        if image[0].isdigit(): #exclude images with only a number as a filename, these are diagnostics
          continue
        else:
          imageList.append(image)
        # print(imageList)
    return imageList

listImages = imageNames(imagedir)



def writeCSV(list, outFile):
  with open(outFile, 'w', newline = '') as csvfile:
    writer = csv.writer(csvfile)
    fieldnames = ['Species']
    writer.writerow(fieldnames)
    for name in list:
      writer.writerow([name])  
  print("saved to file")


writeCSV(listImages, imageFile)