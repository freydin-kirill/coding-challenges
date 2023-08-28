from queue import Queue

def bfs(graph, start, end, max_distance):
    """
    Perform a Breadth-First Search on a graph to find the shortest path
    from the 'start' vertex to the 'end' vertex within the 'max_distance'.
    
    Args:
    graph (List[List[int]]): Adjacency matrix representing the graph.
    start (int): Starting vertex.
    end (int): Ending vertex.
    max_distance (int): Maximum allowed distance for the path.
    
    Returns:
    int: Minimum number of edges in the path from 'start' to 'end', or -1 if no path exists.
    """
    n = len(graph)
    visited = [False] * n  # Keeps track of visited vertices
    distance = [-1] * n     # Stores distance from 'start' to each vertex
    q = Queue()

    q.put(start)
    visited[start] = True
    distance[start] = 0

    while not q.empty():
        u = q.get()
        for v in range(n):
            if not visited[v] and graph[u][v] <= max_distance:
                visited[v] = True
                distance[v] = distance[u] + 1
                q.put(v)
                if v == end:
                    return distance[v]  # Found the shortest path

    return -1  # No valid path found

if __name__ == '__main__':
	# Number of cities
    n = int(input())  
    
    cities = []
	# Read coordinates of each city
    for i in range(n):
        x, y = map(int, input().split())  
        cities.append((x, y))

    max_distance = int(input())  # Maximum travel distance without refueling
    start, end = map(int, input().split())  # Starting and ending cities
    
	# Convert to 0-based indexing
	start -= 1  
    end -= 1
	
	# Initialize the adjacency matrix
    graph = [[0] * n for _ in range(n)]  
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = cities[i]
            x2, y2 = cities[j]
            dist = abs(x1 - x2) + abs(y1 - y2)  # Calculate distance between cities
            graph[i][j] = dist
            graph[j][i] = dist
	
	# Find the shortest path
    print(bfs(graph, start, end, max_distance)) 
