import csv

def readCSVDict(fileName):
  records = {}
  with open(fileName, newline='') as csvfile:
      reader = csv.DictReader(csvfile)
      for row in reader:
          if row['Accepted_name'] != '':
            indexKey = row['Species_name']
            records[indexKey] = row['Accepted_name']
            print (records)
            break
  # print(records[0:5])
  return records

plantNames = readCSVDict('SAPLantChecklistDictb.csv')

def readCSV(fileName):
  list = []
  with open(fileName, newline='') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
          list.append(row[3])
  return list

imageNames = readCSV('FamilyImages_OR.csv')
print(imageNames[0:5])


def matchNames(imageList, namesList):
  checkList = []
  for image in imageNames:
    if image == plantNames[key]:
      indexKey = image
      checkList[indexKey] = plantNames.values()
  
  print(checkList)

  return checkList
matchNames(imageNames, plantNames)
  


