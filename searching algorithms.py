# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:25:36 2017

@author: Yash.Zalavadia
"""
class algo(object):
    
    def insertionSearch(self):
      pass  
    
    def binarySearch(self):
      pass
    
    def interpolationSearch(self):
      pass
    
    def hashTable(self):
      pass



if __name__=="__main__":
    
    b = algo()
    print("1. LINEAR SEARCH \n2.BINARY SEARCH \n3.INTERPOLATION SEARCH \n4.HASH TABLE \n5.EXIT\n")
    a= int(input("Enter number for using algorithm you want to apply:- "))
    
    while a!=5:
        if a==1:
            b.insertionSearch()
            
        elif a==2:
            b.binarySearch()
            
        elif a==3:
            b.interpolationSearch()
        
        elif a==4:
            b.hashTable()
            
        elif a==5:
            exit()
        
        else:   
            print("Incorrect Input, Please enter correct input")
        