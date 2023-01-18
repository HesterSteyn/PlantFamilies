import time, csv
import pandas as pd

namesFile = open('FamilyImages_OR.csv')
masterFile = open('SA-Plant-Checklist-Sep_2022_OR.csv')

# def links(namesFile, masterFile):
    
#     csv_file = csv.reader(namesFile, delimiter=",")

#     csv_file2 = csv.reader(masterFile, delimiter=",")

#     list=[]
#     for row in csv_file2:
#         list.append(row)


#     for row in csv_file:
#         match=False  
#         for secrow in list:                             
#             if row[0].replace(" ","") == secrow[0].replace(" ",""):
#                 print(row[0] + "," + row[1] + "," + secrow[1])
#                 match=True
#         if not match:
#             print(row[0] + "," + row[1] + ", blank no match")
#         time.sleep(1)

#alternative



first = pd.read_csv('FamilyImages_OR.csv')
second = pd.read_csv('SA-Plant-Checklist-Sep_2022_OR.csv')

merged = pd.merge(first, second, how='left', on='Species_name')
merged.to_csv('merged.csv', index=False)