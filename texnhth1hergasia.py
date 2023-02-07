graph = {
    'A' : ['C','D','B'],
    'B' : ['A'],
    'C' : ['E','A'],
    'D' : ['A','E'],
    'E' : ['D','C','F'],
    'F' : ['E','G'],
    'G' : ['F','H'],
    'H' : ['G','I'],
    'I' : ['H','J'],
    'J' : ['I','K'],
    'K' : ['J','L'],
    'L' : ['K','M','N'],
    'M' : ['L','O'],
    'N' : ['L','O'],
    'O' : ['M','N']
}

def bfs(graph, start, end):     #ΕΚΤΕΛΕΣΗ ΤΟΥ BFS ΑΛΓΟΡΙΘΜΟΥ
    queue = [[start]]
    visited=[]
    solution=[]
    while queue:                #ΤΟ ΠΡΟΓΡΑΜΜΑ ΕΚΤΕΛΕΤΑΙ ΟΣΟ ΤΟ queue ΕΧΕΙ ΚΑΠΟΙΑ ΤΙΜΗ
        path = queue.pop(0)     #ΠΑΙΡΝΕΙ ΤΟ ΠΡΩΤΟ ΓΡΑΜΜΑ ΤΟΥ queue ΚΑΙ ΤΟ ΔΙΑΓΡΑΦΕΙ ΑΠΟ ΤΟ queue
        vertex = path[-1]       #ΠΑΙΡΝΕΙ ΤΟ ΤΕΛΕΥΤΑΙΟ ΓΡΑΜΜΑ ΤΟΥ path
        if vertex == end:       #ΕΑΝ ΤΟ vertex ΙΣΟΥΤΑΙ ΜΕ "Ο"
            solution=path       #ΤΟ SOLUTION ΠΑΙΡΝΕΙ ΤΗΝ ΤΙΜΗ ΤΟΥ path
        elif vertex not in visited:                                     #ΕΑΝ Η ΤΙΜΗ ΤΟΥ vertex ΔΕΝ ΥΠΑΡΧΕΙ ΣΤΗΝ visited ΤΟΤΕ ΕΚΤΕΛΕΙ ΤΗΝ ELIF
            for neighbour in graph.get(vertex, []):                     #ΤΟ neighbour ΠΑΙΡΝΕΙ ΤΗΝ  ΤΙΜΗ ΤΩΝ ΚΟΡΥΦΩΝ ΠΟΥ ΣΥΝΔΕΟΝΤΑΙ ΜΕ ΤΟ vertex
                new_path = list(path)                                   #Το new_path ΠΑΙΡΝΕΙ ΤΟ path
                new_path.append(neighbour)                              #ΤΟ new_path ΠΑΙΡΝΕΙ ΤΗΝ ΤΙΜΗ ΤΟΥ neighbour
                queue.append(new_path)                                  #ΣΤΟ queue ΠΡΟΣΤΙΘΕΤΑΙ ΤΟ new_path
                if (neighbour == end): 
                    solution=new_path
            visited.append(vertex)                                      #ΜΕΤΑ ΤΟ ΤΕΛΟΣ ΤΗΣ FOR ΣΤΟ visited ΠΡΟΣΤΙΘΕΤΑΙ ΤΟ vertex
    visited.append(end)
    print("Bfs path is",visited)
    print("The solution using Bfs is",solution)
bfs(graph, 'A', 'O')


visited = []
solution=""
def dfs(visited, graph, node,end,solution):     #ΕΚΤΕΛΕΣΗ ΤΟΥ DFS ΑΛΓΟΡΙΘΜΟΥ   
    if node not in visited: 
        solution+=node+","                  
        if node==end:
          print("Dfs path and solution is",solution[:-1])
          exit()
        visited.append(node)                 #ΕΙΣΑΓΕΙ ΜΕΣΑ ΣΤΗΝ visited ΤΟΝ ΚΟΜΒΟ ΠΟΥ ΕΠΙΣΚΕΦΤΗΚΕ
        for neighbour in graph[node]:        #ΤΟ neighbour ΠΑΙΡΝΕΙ ΤΗΝ  ΤΙΜΗ ΤΩΝ ΚΟΡΥΦΩΝ ΠΟΥ ΣΥΝΔΕΟΝΤΑΙ ΜΕ ΤΟ node
            dfs(visited, graph, neighbour,end,solution)     #ΔΙΑΒΑΖΕΙ ΤΗΝ ΠΡΩΤΗ ΚΟΡΥΦΗ ΠΟΥ ΣΥΝΔΕΕΤΑΙ ΜΕ ΤΟ node ΚΑΙ ΚΑΛΕΙ ΞΑΝΑ ΤΟΝ ΑΛΓΟΡΙΘΜΟ
dfs(visited, graph, 'A','O',solution)
