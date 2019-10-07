"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy



class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Can't create edge based on the given vertices.")

        
    """
    Pseudocode for breadth-first traversal (BFT)
    Create a Queue
    Create a list of visited nodes
    Put starting node in the queue
    While queue is not empty
        Pop first node out of queue
        if Not visited, mark it as visited - get adjacent nodes and add to list
    go to top of loop
    """

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        print("Breadth First Transversal of the graph: ")
        qq = Queue()
        visited = set()

        qq.enqueue(starting_vertex)
        while qq.size() > 0:
            vertex = qq.dequeue()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)

                for next_vert in self.vertices[vertex]:
                    qq.enqueue(next_vert)



    """
    Pseudocode for depth-first traversal (DFT)
    Create a stack
    Create a list of visited nodes
    Put starting node in the stack
    While stack is not empty
        Pop first node out of stack
        If not visited, mark it visited and add adjacent

    """
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        print("Depth-first traversal of the graph: ")
        ss = Stack()
        visited = set()

        ss.push(starting_vertex)

        while ss.size() > 0:
            vertex = ss.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)

                for next_vert in self.vertices[vertex]:
                    ss.push(next_vert)
    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if not visited:
            visited = set()

        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
        
            for next_ver in self.vertices[starting_vertex]:
                self.dft_recursive(next_ver, visited)
        
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        qq = Queue()
        visited_nodes = set()

        # We are going to store paths instead of single nodes in the queue for this one.
        # Starting vertex is stored as a list instead of a single value so we can add to it
        qq.enqueue([starting_vertex])
        while qq.size() > 0:

            # Take the route out, and the last vertex in the route
            route = qq.dequeue()
            vertex = route[-1]

            # If we haven't been to the last vertex yet, great! Lets take a look at it.
            if vertex not in visited_nodes:

                # If the last vertex in our route is the destination_vertex (the node we are looking for), we simply return the route.
                if vertex is destination_vertex:
                    return route

                # Otherwise, we need to keep looking for our destination.
                else:

                    # Add the vertex to the visited set, so we don't check it twice
                    visited_nodes.add(vertex)

                    # And then take all of its neighbors (specifically the connections to those neighbors),
                    # and create a copy of our route with each of those connections added
                    # This way we enqueue all possible routes from the current node, to the next nodes in our graph.
                    for edge in self.vertices[vertex]:
                        route_copy = route.copy()
                        route_copy.append(edge)
                        qq.enqueue(route_copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        # This one has a very similar setup to the BFS implementation so I won't notate it as well.
        # The real difference is in which nodes we choose to visit next -- based on popping from the stack versus dequeuing from a queue
        # but as far as implementation goes, they are virtually identical.
        depth_search_stack = Stack()
        visited_nodes = set()

        depth_search_stack.push([starting_vertex])

        while depth_search_stack.size() > 0:
            route = depth_search_stack.pop()
            vertex = route[-1]

            if vertex not in visited_nodes:
                if vertex is destination_vertex:
                    return route
                visited_nodes.add(vertex)
                for edge in self.vertices[vertex]:
                    route_copy = route.copy()
                    route_copy.append(edge)
                    depth_search_stack.push(route_copy)






if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('DFT RECURSIVE =-=-=-=-=')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
