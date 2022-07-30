graph = { 1:[2,3],
          2:[1,4,7,5],
          3:[1,6,4],
          4:[2,3,5],
          5:[2,4],
          6:[3,7],
          7:[6,2]
        }
    
visited = []
node = int(input("Enter first node: "))

def DFS(node,visited,graph):
    
    if node not in graph:
        print("Node is not present")
        return 
    
    if node not in visited:
        print(node,end =" ")
        visited.append(node)
        
        for i in graph[node]:
            DFS(i,visited,graph)
            
print("Not visited elements")        
DFS(node,visited,graph)
if(len(visited) != 0):
    print()
    print("After visiting element")
    print(visited)