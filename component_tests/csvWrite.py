#IMPORTS
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#Basics
import time
import csv

#CLASS DEFINITIONS
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class DataManager:

    def __init__(self):
        self.content=[0,0]
        self.numRows = 0
        self.fileIndex = 0
        self.currentFile = open('data0.csv', 'w')
        self.writer = csv.writer(self.currentFile)

    def record(self):   #UNTESTED
        self.numRows += 1
        self.updateTime(time.time())
        self.writer.writerow(self.content)
        if (self.numRows > 1000):   #Maximum file size reached
            self.currentFile.close()
            self.fileIndex += 1
            print('Creating new file... name: '+'data'+str(self.fileIndex)+'.csv')
            self.currentFile = open('data'+str(self.fileIndex)+'.csv', 'w')
            self.writer = csv.writer(self.currentFile)
            self.numRows = 0

    def updateTime(self, timeStamp):
        self.content[0] = timeStamp
        self.content[1] = self.numRows

    def cleanUp(self):
        self.currentFile.close()

#/////////////////////////////////////////////////////////

#MAIN
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
if __name__ == '__main__':
    #Main Loop
    data = DataManager()
    for i in range(3500):
        data.record()
        time.sleep(0.01)
    pass
#/////////////////////////////////////////////////////////