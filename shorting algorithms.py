# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:25:36 2017

@author: Yash.Zalavadia
"""
class algo(object):
    
    def bubbleSort(self):
      pass  
    
    def insertionSort(self,myList):
        i="Null"
        key="Null"
        for j in range(1,len(myList)):
            key=myList[j]
            i=j-1
            while i>=0 and myList[i]>key:
                myList[i+1]=myList[i]
                i=i-1
            myList[i+1]=key
        return myList
    
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
    flag=True
        
    while flag==True:
        print("1. BUBBLE SORT \n2.INSERTION SORT \n3.SELECTION SORT \n4.MERGE SORT \n5.SHELL SHORT \n6.QUICK SORT \n7. HEAP SORT \n8.COUNT SORT \n9.EXIT\n")
        a= int(input("Enter number for using algorithm you want to apply:- "))

        if a==1:
            b.bubbleSort()
            
        elif a==2:
            l=[int(x) for x in input().split(" ")]
            print(b.insertionSort(l))
            
            
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
        
