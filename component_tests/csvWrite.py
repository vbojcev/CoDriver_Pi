#IMPORTS
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#Basics
import time
import csv

#CLASS DEFINITIONS
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class DataManager:

    def __init__(self):
        self.content=[0]
        self.numRows = 0
        self.fileIndex = 0
        self.currentFile = open('data0.csv', 'w', newline='')
        self.writer = csv.writer(self.currentFile)

    def record(self):   #UNTESTED
        self.updateTime(time.time())
        self.writer.writerow(self.content)
        self.numRows += 1
        if (self.numRows > 1000):   #Maximum file size reached
            self.currentFile.close()
            self.fileIndex += 1
            self.currentFile = open('data'+str(self.fileIndex)+'.csv', 'w', newLine='')
            self.writer = csv.writer(self.currentFile)
            self.numRows = 0

    def updateTime(self, timeStamp):
        self.content[0] = timeStamp

#/////////////////////////////////////////////////////////

#MAIN
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
if __name__ == '__main__':
    #Main Loop
    pass
#/////////////////////////////////////////////////////////