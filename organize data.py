# -*- coding: utf-8 -*-

"""
Created on Mon Oct  9 17:25:36 2017

@author: Yash.Zalavadia
"""
class stack_queue_algo(object):
    
    def stack(self):
      flag = True
      while flag:
          print("1. Enter Element 2.Delete Element 3.Display Stack\n")
          a=int(input("Enter your choice: "))
          if a==1:
            b.push_stack()
          if a==2:
            b.pop()
          if a==3:
            b.display()

    def queue(self):
        flag = True
        while flag:
          print("1. Enter Element 2.Delete Element 3.Display Stack\n")
          a=int(input("Enter your choice: "))
          if a==1:
            b.push_queue()
          if a==2:
            b.pop()
          if a==3:
            b.display()
            
    def push_stack(self,l):
        self.element=int(input("Enter number you want to add to stack: "))
        l.append(self.element)
        
    def push_queue(self,l):
        self.element=int(input("Enter number you want to add : "))
        l.insert(0,self.element)
        
    def pop(self,l):
        if len(l)==0:
            print("The list is already Empty")
            return
        l.pop()
        
    def display(self,l):
        return l
    
class linkedList:
     def singlyLinkedList(self):
      pass  
    
    def doublyLinkedList(self):
      pass
    
if __name__=="__main__":
    
    b = stack_queue_algo()
    l = linkedList()
    
    while a!=5:
        print("1. STACK \n2.QUEUE \n3.SINGLY LINKED LIST \n4.DOUBLY LINKED LIST \n5.EXIT\n")
        a = int(input("Enter number for using DATA STRUCTURE you want to apply:- "))
    
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
        
