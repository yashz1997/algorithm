# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:25:36 2017

@author: Yash.Zalavadia
"""
class algo(object):
    
    def bubbleSort(self):
      pass  
    
    def insertionSort(self):
      pass
    
    def selectionSort(self):
      pass
    
    def mergeSort(self):
      pass
    
    def shellSort(self):
      pass
    
    def quickSort(self):
      pass
    
    def heapSort(self):
      pass
    
    def countSort(self):
      pass


if __name__=="__main__":
    
    b = algo()
    print("1. BUBBLE SORT \n2.INSERTION SORT \n3.SELECTION SORT \n4.MERGE SORT \n5.SHELL SHORT \n6.QUICK SORT \n7. HEAP SORT \n8.COUNT SORT \n9.EXIT\n")
    a= int(input("Enter number for using algorithm you want to apply:- "))
    
    while a!=9:
        if a==1:
            b.bubbleSort()
            
        elif a==2:
            b.insertionSort()
            
        elif a==3:
            b.selectionSort()
        
        elif a==4:
            b.mergeSort()
            
        elif a==5:
            b.insertionSort()
            
        elif a==6:
            b.shellSort()
            
        elif a==7:
            b.heapSort()
            
        elif a==8:
            b.countSort()
            
        elif a==9:
            exit()
        
        else:   
            print("Incorrect Input, Please enter correct input")
        