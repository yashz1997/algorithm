# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 17:25:36 2017

@author: Yash.Zalavadia
"""
class algo(object):
    
    def treeTraversal(self):
      pass  
    
    def binarySearchTree(self):
      pass
    
    def avlTree(self):
      pass
    
    def spaningTree(self):
      pass

    def heap(self):
      pass


if __name__=="__main__":
    
    b = algo()
    print("1. TREE TRAVERSAL \n2.BINARY SEARCH TREE \n3.AVL TREE \n4.SPANNING TREE \n5.HEAP \n6.EXIT\n")
    a= int(input("Enter number for using algorithm you want to apply:- "))
    
    while a!=6:
        if a==1:
            b.treeTraversal()
            
        elif a==2:
            b.binarySearchTree()
            
        elif a==3:
            b.avlTree()
        
        elif a==4:
            b.spaningTree()
            
        elif a==4:
            b.heap()
            
        elif a==6:
            exit()
        
        else:   
            print("Incorrect Input, Please enter correct input")
        # -*- coding: utf-8 -*-

