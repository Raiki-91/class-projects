"""
Program Name: CIS110 Final04
Program Description: class definition for packages
Author Name: Lee Kitchen
Date Created: 8/31/201
Notes: class def for Packages


"""
import time
import random
class Package:
    trackernum= random.randrange(0,(100**5))
    arrived= False
    loaded= False
    def __init__(self,length, width, height, dzip, weight):
        self.length= length
        self.width= width
        self.height= height
        self.dzip= dzip
        self.weight= weight

        
    def tracker(self):
        return self.trackernum
    
    def volume(self):
        self.volume= self.length*self.width*self.height
        return self.volume
    
    def dzip(self):
        return self.dzip
    
    def delivered(self):
        if arrived == True:
            return "Delivered",time.asctime( time.localtime(time.time()))
        else:
            return "Not Delivered"
    def isLoaded(self, loaded):
        loaded= self.loaded
        if loaded is True:
            return self.loaded
        else:
            return False
    
    def setStatus(self,status):
        arrived= status
        return arrived

    def __str__(self):
        return" {}, {}".format(self.tracker ,self.dzip)
    
def main():
    
    if __name__ == '__main__':
        main()
