# -*- coding: utf-8 -*-

"""
Created on Mon Oct  9 17:25:36 2017

@author: Yash.Zalavadia
"""
class stack_queue_algo(object):
    l=[]
    def stack(self):
      flag = True
      while flag:
          print("1. Enter Element 2.Delete Element 3.Display Stack\n")
          a=int(input("Enter your choice: "))
          if a==1:
            b.push_stack(self.l)
          if a==2:
            b.pop(self.l)
          if a==3:
            b.display()

    def queue(self):
        flag = True
        while flag:
          print("1. Enter Element 2.Delete Element 3.Display Queue\n")
          a=int(input("Enter your choice: "))
          if a==1:
            b.push_queue(self.l)
          if a==2:
            b.pop(self.l)
          if a==3:
            b.display()
            
    def push_stack(self,l):
        element=int(input("Enter number you want to add to stack: "))
        l.append(element)
        
    def push_queue(self,l):
        element=int(input("Enter number you want to add : "))
        l.insert(0,element)
        
    def pop(self,l):
        if len(l)==0:
            print("The list is already Empty")
            return
        self.l =l[0:-1] 
        
    def display(self):
        print(self.l)
    
class linkedList:
     def singlyLinkedList(self):
      pass  
    
     def doublyLinkedList(self):
      pass
    
if __name__=="__main__":
    
    b = stack_queue_algo()
    l = linkedList()
    print("1.STACK \n2.QUEUE \n3.SINGLY LINKED LIST \n4.DOUBLY LINKED LIST \n5.EXIT\n")
    a = int(input("Enter number for using DATA STRUCTURE you want to apply:- "))
    
    while a!=5:
        
        if a==1:
            b.stack()
            
        elif a==2:
            b.queue()
            
        elif a==3:
            l.singlyLinkedList()
        
        elif a==4:
            l.doublyLinkedList()
            
        elif a==5:
            exit()
        
        else:   
            print("Incorrect Input, Please enter correct input")
        
