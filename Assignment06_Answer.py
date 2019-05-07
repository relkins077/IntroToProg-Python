#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Changed the code to match the assignment.
#   Now each row is a dictionary and the table is a list!
#   RRoot, 11/03/2016, Moved processing and IO code into classes and methods
#-------------------------------------------------#

## Data #############################################
strFileName = "C:\_PythonClass\Todo.txt"
strChoice = ""
blnStatus = False
dicRowOfData = {}
lstTableOfData = []
## Data #############################################

## Input/0utput ####################################
class IO:
    @staticmethod
    def InputTaskToAdd():
        ''' Ask which task they want to add
        :return: tuple of strings (Task,Priority)
        '''
        strTask = str(input("What is the task? - ")).strip()
        strPriority = str(input("What is the priority? [high|low] - ")).strip()
        return strTask, strPriority
    #end function/method

    @staticmethod
    def InputTaskToDelete():
        ''' Ask which task they want to delete
        :return: string
        '''
        return str(input("Which TASK would you like removed? - ")).strip()
    #end function/method

    @staticmethod
    def InputSaveToFile():
        ''' Ask the user if they want to save to file (and verify)
        :return: string
        '''
        return str(input("Save this data to file? (y/n) - ")).strip().lower()
    #end function/method

    @staticmethod
    def InputMenuChoice():
        ''' Gets the menu choice from a user
        :return:
        '''
        strChoice = str(input("Which option would you like to perform? [1 to 6] - ")).strip()
        return strChoice
    #end function/method

    @staticmethod
    def OutputMenuItems():
        '''  Display a menu of choices to the user
        :return: string
        '''
        print ("""
        Menu of Options
        1) Show current data
        2) Add a new item.
        3) Remove an existing item.
        4) Save Data to File
        5) Reload Data from File
        6) Exit Program
        """)
        print()#adding a new line
    #end function/method

    @staticmethod
    def OutputCurrentTasks(TableOfData):
        ''' Show the current items in the table
        :return: None
        '''
        print()#adding a new line
        print("******* The current items ToDo are: *******")
        for row in TableOfData: print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        print()#adding a new line
    #end function/method

    @staticmethod
    def OutputAdditonStatus(WasItemAdded):
        # 5b-Update user on the status
        print()#adding a new line
        if (WasItemAdded == True): print("The task was added.")
        else: print("An Error has occurred")# We will talk about error handling later!
        print()#adding a new line
    #end function/method

    @staticmethod
    def OutputDeletionStatus(WasItemRemoved):
        # 5b-Update user on the status
        print()#adding a new line
        if (WasItemRemoved == True): print("The task was removed.")
        else: print("I'm sorry, but I could not find that task.")
        print()#adding a new line
    #end function/method
#end class
## Input/0utput ####################################

## Data Processing #################################
class DataProcessor:
    @staticmethod
    def GetDataFromFile(FileName, TableOfData):
        ''' Load the  data from a text file called ToDo.txt into a python Dictionary.
        :arg input FileName = Name of file to use,
             output TableOfData = ref to a 2 dimension list[dic{}] object
        :return: None
        '''
        objFile = open(FileName, "r")
        for line in objFile:
            strData = line.split(",") # readline() reads a line of the data into 2 elements
            dicRow = {"Task":strData[0].strip(), "Priority":strData[1].strip()}
            TableOfData.append(dicRow)
        objFile.close()
    #end function/method

    @staticmethod
    def InsertTask(Task, Priority, TableOfData):
        '''Add a new item to the list/Table
        :arg Task = New Task to add,
             Priority = New Priority to add
        :return: None
        '''
        dicRow = {"Task":Task,"Priority":Priority}
        TableOfData.append(dicRow)
    #end function/method

    @staticmethod
    def DeleteTask(KeyToRemove, TableOfData):
        '''5a-Allow user to indicate which row to delete
        :arg input KeyToRemove = Name of Key in the dic{} you want to remove,
             output TableOfData = ref to a 2 dimension list[dic{}] object
        :return: Boolean
        '''
        blnWasItemRemoved = False  # Creating a boolean Flag
        intRowNumber = 0
        while (intRowNumber < len(TableOfData)):
            if (KeyToRemove == str(list(dict(TableOfData[intRowNumber]).values())[0])): # the values function creates a list!
                del TableOfData[intRowNumber] #Add Error handling!
                blnWasItemRemoved = True
            # end if
            intRowNumber += 1
        # end for loop
        return blnWasItemRemoved
    #end function/method

    def InsertDataToFile(FileName, TableOfData):
        '''
        :arg input FileName = Name of file to use,
             output TableOfData = ref to a 2 dimension list[dic{}] object
        :return:
        '''
        objFile = open(FileName, "w")
        for dicRow in TableOfData:
            objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        objFile.close()
    #end function/method
#end class
## Data Processing #################################

## MAIN ############################################
# Step 1 When the program starts, load the any data you have in a
# text file called ToDo.txt into a python Dictionary.
DataProcessor.GetDataFromFile(strFileName,lstTableOfData)
while(True):
    IO.OutputMenuItems()# Step 2 Display a menu of choices to the user
    strChoice = IO.InputMenuChoice().strip()# and get their selection

    if (strChoice == '1'): #Step 3 - Show the current items in the table
        IO.OutputCurrentTasks(lstTableOfData)
        continue

    elif(strChoice == '2'): #Step 4 - Add a new item to the list/Table
        strTask, strPriority = IO.InputTaskToAdd()#Ask user for a Task and Priority to Add
        DataProcessor.InsertTask(strTask, strPriority, lstTableOfData)#Add the row if you can
        IO.OutputCurrentTasks(lstTableOfData)#Show the current items in the table
        continue #to show the menu

    elif(strChoice == '3'): # Step 5 - Remove a new item to the list/Table
        strKeyToRemove = IO.InputTaskToDelete()#Ask user which row to delete
        blnStatus = DataProcessor.DeleteTask(strKeyToRemove,lstTableOfData)#Delete the row if you can
        IO.OutputDeletionStatus(blnStatus)#Show the result of the deletion
        IO.OutputCurrentTasks(lstTableOfData)#Show the current items in the table
        continue #to show the menu

    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        IO.OutputCurrentTasks(lstTableOfData)#5a Show the current items in the table
        if("y" == IO.InputSaveToFile()): #5b Ask if they want save that data
            DataProcessor.InsertDataToFile(strFileName, lstTableOfData)
            #input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
            pass
            #input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        continue #to show the menu

    elif (strChoice == '5'):
        lstTableOfData.clear() #clear list's data before re-loading
        DataProcessor.GetDataFromFile(FileName=strFileName, TableOfData=lstTableOfData)#Get data from file
        IO.OutputCurrentTasks(lstTableOfData)#Show the current items in the table
        continue  # to show the menu

    elif (strChoice == '6'):
        break #and Exit the program
## MAIN ############################################
