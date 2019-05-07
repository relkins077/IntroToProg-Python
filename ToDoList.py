#-------------------------------------------------#
# Title: Functions
# Dev:   RElkins
# Date:  May, 7, 2019
# ChangeLog: (Who, When, What)
#  RElkins, 5/7/19, modified prior code to functions

#-------------------------------------------------#

## Data variables ####
strFileName = "C:\_PythonClass\Assignment06\ToDo.txt"
blnStatus = False
dicRowOfData = {}
lstTableOfData = []


#-- Input/Output --#
# User can see a Menu (Step 2)
def Menu():
    '''  Display menu '''
    print ("""
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Remove an existing item.
        4) Save Data to File
        5) Reload Data from File
        6) Exit Program
        """)

# User can see data (Step 3)
def OutputData(data):
    print('The list of data is:')
    for row in data: print(row["Task"] + "(" + row["Priority"] + ")")


# User can insert or delete data(Step 4 and 5)
def AddTask():
    strTask = input("Enter your task here: ") # input item
    strPri = input("Enter the priority: ") # input priority
    return strTask, strPri

def DelTask():
    return str(input("What task do you want to remove? "))

# User can save to file (Step 6)
def SaveFile():
    return input("Save? Y or N: ")

def LoadData(FileName, Data):
    f = open(FileName,"r") #opens file with name of "todo.txt"

    for line in f:
        strData = line.split(",")
        dicRow = {"Task":strData[0].strip(), "Priority":strData[1].strip()}
        Data.append(dicRow)
    f.close()

def LoadTask(Task, Priority, Data):
    dicRow = {"Task":Task,"Priority":Priority}
    Data.append(dicRow)

def InsertData(FileName, Data):
    f = open(FileName, "w")
    for dicRow in Data:
        f.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
    f.close()

def DeleteTask(DelItem,Data):
    if DelItem in Data:
        del Data[int(DelItem)]
#-- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python List and Dictionary.
LoadData(strFileName,lstTableOfData)

while True:
    Menu()
    strUserValue = str(input("Select a value"))
    if (strUserValue.strip() == '1'):
        OutputData(lstTableOfData)
    elif (strUserValue.strip() == '2'):
        strTask, strPriority = AddTask()
        LoadTask(strTask, strPriority, lstTableOfData)
    elif (strUserValue.strip() == '3'):
        DelItem = DelTask()
        DeleteTask(DelItem, lstTableOfData)

    elif (strUserValue.strip() == '4'):
        if("y" == SaveFile()):
            InsertData(strFileName, lstTableOfData)
        else:
            print("No data saved")
    elif (strUserValue.strip() == '5'):
        LoadData(strFileName,lstTableOfData)
    elif (strUserValue.strip() == '6'):
        exit()



