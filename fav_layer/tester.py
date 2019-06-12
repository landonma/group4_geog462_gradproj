import os

hiddenExists = os.path.isfile('Lists\\hiddenlist.txt')
displayedExists = os.path.isfile('displayedlist.txt')


if hiddenExists:
    hiddenList =[line.rstrip('\n') for line in open("Lists\\hiddenlist.txt")]

if not hiddenExists:
    hiddenList = open("Lists\\hiddenlist.txt", "w+")
    hiddenList =[line.rstrip('\n') for line in open("Lists\\hiddenlist.txt")]


if displayedExists:
    displayedList =[line.rstrip('\n') for line in open("Lists\\displayedlist.txt")]

if not displayedExists:
    displayedList = open("Lists\\displayedlist.txt", "w+")
    displayedList =[line.rstrip('\n') for line in open("Lists\\displayedlist.txt")]


filepath=r'C:\Users\Mark\Downloads\Fire Project-20190304T000216Z-001\Fire Project\FireProject\FireProject.tbx'
filepath = filepath.split('\\')
cleanpath = filepath[-2] + '\\' + filepath[-1]
print(cleanpath)

hiddenList.append("list.file.path")
with open("Lists\\displayedlist.txt", "w+") as f:
    for lines in hiddenList:
        f.write("%s\n" % lines)

#for lines in hiddenList:


#if not len(displayedList) == len(hiddenList):

hiddenExists = os.path.isfile('C:\\Users\\Mark\\Documents\\fav_layerLists\\hiddenlist.txt')
print(hiddenExists)