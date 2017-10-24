# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:25:36 2017

@author: Yash.Zalavadia
"""
class algo(object):
    
    def bubbleSort(self):
        flag=True
        while flag:
            flag=False
            for x in range(len(myList)-1):
                if myList[x]>myList[x+1]:
                    flag=True
                    temp=myList[x]
                    myList[x]=myList[x+1]
                    myList[x+1]=temp
        return myList  
    
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
    
    def selectionSort(self,myList):       // Not Solved
        i=0
        for x in range(i,len(myList)+1):
            k = min(myList[i:]) 
	        print(myList.index(k))
	        if myList[x]>k:
	           temp = myList[x]
	           myList[x] = k
   	           myList[myList.index(k)] = temp
   	        i =i+1	       
        return myList
    
    def mergeSort(self):
      pass
    
    def shellSort(self):
      pass
    
    def quickSort(self):
        less = []
        equal = []
        greater = []
        flag = myList[0]

        for x in myList:
            if x<flag:
                less.append(x)
            elif x == flag:
                equal.append(x)
            elif x>flag:
                greater.append(x)

        less.sort(); equal.sort(); greater.sort() 
        l=less+equal+greater
        return l
    
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
        l=[int(x) for x in input("Enter elements seperated by commas: ").split(",")]
        
        if a==1:
            print(b.bubbleSort(l))
            
        elif a==2:
            print(b.insertionSort(l))
                        
        elif a==3:
            print(b.selectionSort(l))
        
        elif a==4:
            b.mergeSort()
            
        elif a==5:
            b.shellSort()
            
        elif a==6:
            print(b.quickSort(l))
            
        elif a==7:
            b.heapSort()
            
        elif a==8:
            b.countSort()
            
        elif a==9:
            exit()
        
        else:   
            print("Incorrect Input, Please enter correct input")
