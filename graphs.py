# -*- coding: utf-8 -*-

"""
Created on Mon Oct  9 17:25:36 2017

@author: Yash.Zalavadia
"""
class algo(object):
    
    def dfs(self,graph, start, end, path=[]):
        path = path + [start] 
        if start == end: 
            return path 
        for node in graph[start]: 
            if node not in path: 
                newpath = find_path(graph, node, end, path) 
                if newpath: return newpath 
        return None
    
    def bfs(self):
      pass

    def dijkstra(self):
      pass   

find_path(graph, "A", "D")
    
if __name__=="__main__":
    
    b = algo()
    print("1.DFS \n2.BFS \n3.DIJKSTRA \n4.EXIT\n")
    a= int(input("Enter number for using algorithm you want to apply:- "))
    graph = {'A': ['B', 'C'], 
              'B': ['F'], 
              'C': ['D'], 
              'D': ['C'], 
              'E': ['F'], 
              'F': ['E']} 

    while a!=4:
        if a==1:
            print(b.dfs(graph,"A","D"))
            
        elif a==2:
            b.bfs()
            
        elif a==3:
            b.dijkstra()
        
        elif a==4:
            exit()
        
        else:   
            print("Incorrect Input, Please enter correct input")
            
           
        
        
