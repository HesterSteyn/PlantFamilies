import os
import csv
from csv import reader
from pathlib import Path

imagedir = r'H:\2023 Copy CPF images_Names corrected'
imageFile = 'temp.csv'
filetypes = ['.jpg', '.jpeg', '.tif', '.tiff']

def imageNames(dir):
  imageList = []
  for root, dirs, files in os.walk(dir):
    for file in files:
      fileExt = Path(file).suffix
      if fileExt.lower() in filetypes:
        if file[0].isdigit(): #exclude images starting with a number in a filename
          continue
        else:
          imageList.append(Path(file).stem)
      
  uniques = set(imageList)
  print(len(imageList), 'images in total')
  print(len(uniques), 'unique image names')
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