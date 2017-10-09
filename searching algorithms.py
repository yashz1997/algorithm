# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:25:36 2017

@author: Yash.Zalavadia
"""
class algo(object):
    
    def insertionSearch(self):
      pass  
    
    def binarySearch(self,no,myList):
        self.found=False
        self.bottom=0
        self.top=len(myList)-1
    
        while self.bottom <= self.top and self.found==False:
            self.middle=(self.bottom+self.top)//2
            if no==myList[self.middle]:
                return self.middle
            elif self.middle<no:
                self.bottom=self.middle+1
            elif self.middle>no:
                self.top=self.middle-1
    
    def interpolationSearch(self):
      pass
    
    def hashTable(self):
      pass



if __name__=="__main__":
    
    b = algo()
    flag=True
    
    
    while flag==True:
        print("1. LINEAR SEARCH \n2.BINARY SEARCH \n3.INTERPOLATION SEARCH \n4.HASH TABLE \n5.EXIT\n")
        a= int(input("Enter number for using algorithm you want to apply:- "))
        if a==1:
            b.insertionSearch()
            
        elif a==2:
            
            l=[3,5,8,56,66,85]
            no=int(input("Enter number you want to search: "))
            pos=b.binarySearch(no,l)
            if pos:
                print("Position of your item is %s"%pos)
            else:
                print("No such item found in your list")
                    
            
        elif a==3:
            b.interpolationSearch()
        
        elif a==4:
            b.hashTable()
            
        elif a==5:
            exit()
        
        else:   
            print("Incorrect Input, Please enter correct input")
        
