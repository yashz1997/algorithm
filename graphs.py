# -*- coding: utf-8 -*-

"""
Created on Mon Oct  9 17:25:36 2017

@author: Yash.Zalavadia
"""
class algo(object):
    
    def dfs(self):
      pass
    
    def bfs(self):
      pass

    def dijkstra(self):
      pass  
    
    
    
if __name__=="__main__":
    
    b = algo()
    print("1.DFS \n2.BFS \n3.DIJKSTRA \n4.EXIT\n")
    a= int(input("Enter number for using algorithm you want to apply:- "))
    
    while a!=4:
        if a==1:
            b.dfs()
            
        elif a==2:
            b.bfs()
            
        elif a==3:
            b.dijkstra()
        
        elif a==4:
            exit()
        
        else:   
            print("Incorrect Input, Please enter correct input")
        