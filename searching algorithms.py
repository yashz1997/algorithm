# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:25:36 2017

@author: Yash.Zalavadia
"""
class algo(object):
    
    
    def linearSearch(self,no,myList):
        count = 0 
        for x in myList:
            if no==x:
                return count
            count += 1
    
    def binarySearch(self,no,myList):
        found=False
        bottom=0
        top=len(myList)-1
    
        while bottom <= top and found==False:
            middle=(bottom+top)//2
            if no==myList[middle]:
                return middle
            elif myList[middle]<no:
                bottom=middle+1
            elif myList[middle]>no:
                top=middle-1
    
    def interpolationSearch(self,no,myList,n):
        
        bottom = 0
        top = n-1
        print(top)
        while bottom<=top and no>=myList[bottom] and no<=myList[top]:
            pos = bottom + int(((float(top-bottom) / (myList[top] -myList[bottom])) * (no - myList[bottom])))
            if no==myList[pos]:
                return pos
            elif myList[pos]<no:
                bottom=pos+1
            elif myList[pos]>no:
                top=pos-1



if __name__=="__main__":
    
    b = algo()
    flag=True
    
    
    while flag==True:
        
        print("1.LINEAR SEARCH \n2.BINARY SEARCH \n3.INTERPOLATION SEARCH  \n4.EXIT\n")
        a= int(input("Enter number for using algorithm you want to apply:- "))
        
        if a!=5:
            l=[int(x) for x in input("Input Numbers seperated by comma: ").split(",")]      
            no= int(input("Enter number you want to search : "))
            
        if a==1:
            pos = b.linearSearch(no,l)
            print(pos)
            if pos!= "NULL":
                print("Position of your item is %s" %pos)
            else:
                print("No such item found in your list")
            
            
        elif a==2:
            
            pos = b.binarySearch(no,l)
            print(pos)
            if pos!= "NULL":
                print("Position of your item is %s" %pos)
            else:
                print("No such item found in your list")
                    
            
        elif a==3:
            length = len(l)
            pos = b.interpolationSearch(no,l,length)
            print(pos)
            if pos!= "NULL":
                print("Position of your item is %s" %pos)
            else:
                print("No such item found in your list")
        
        elif a==4:
            exit()
        
        else:   
            print("Incorrect Input, Please enter correct input")
        
