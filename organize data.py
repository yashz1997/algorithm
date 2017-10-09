# -*- coding: utf-8 -*-

"""
Created on Mon Oct  9 17:25:36 2017

@author: Yash.Zalavadia
"""
class algo(object):
    
    def stack(self):
      pass
    
    def queue(self):
      pass

    def singlyLinkedList(self):
      pass  
    
    def doublyLinkedList(self):
      pass
    
    
if __name__=="__main__":
    
    b = algo()
    print("1. STACK \n2.QUEUE \n3.SINGLY LINKED LIST \n4.DOUBLY LINKED LIST \n5.EXIT\n")
    a= int(input("Enter number for using algorithm you want to apply:- "))
    
    while a!=5:
        if a==1:
            b.stack()
            
        elif a==2:
            b.queue()
            
        elif a==3:
            b.singlyLinkedList()
        
        elif a==4:
            b.doublyLinkedList()
            
        elif a==5:
            exit()
        
        else:   
            print("Incorrect Input, Please enter correct input")
        