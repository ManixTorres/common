import collections
from operator import truediv
import numpy



arr = []
x = open("yeahdamn.txt", "r")
xprime = x.readlines()
for words in xprime:
    arr.append(words.strip("\n"))
    
begin, finish = arr[0].split()
n = int(begin) ## number of nodes
del arr[0]
dict = {}


for z in arr:
    first,second = z.split()
    if (int(first) not in dict):
        dict[int(first)] = [int(second)]
    else:
        dict[int(first)].append(int(second))    
            
    
def dfs(j, visit, visited, graph): 
    visit[j-1] = 1
    if j not in graph:
        graph[j] = []
    
    for next in graph[j]:
        if visit[next-1] == 0:
            dfs(next, visit, visited, graph)
    visited.append(j)        
    return 0

graph = collections.OrderedDict(dict.items())
visit = numpy.zeros(n, dtype = bool)
order = numpy.zeros(n, dtype = int)


def tSort(graph):
    index = n - 1 # index for the vertices
    for j in range(1, n+1):
        if visit[j-1] == False:
            visitedNodes = []
            dfs(j,visit,visitedNodes,graph)
            for y in visitedNodes: ##backwards output
                order[index] = y
                index = index - 1           
    return order


    
print(tSort(graph))        