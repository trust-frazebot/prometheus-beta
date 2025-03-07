from typing import List, Dict
from collections import deque

class DinicMaxFlow:
    def __init__(self, num_vertices: int):
        """
        Initialize the Dinic's algorithm max flow graph.
        
        :param num_vertices: Total number of vertices in the graph
        """
        self.num_vertices = num_vertices
        self.graph = [[] for _ in range(num_vertices)]
        self.flow_graph = [[] for _ in range(num_vertices)]
    
    def add_edge(self, u: int, v: int, capacity: int):
        """
        Add an edge to the graph with given capacity.
        
        :param u: Source vertex
        :param v: Destination vertex
        :param capacity: Edge capacity
        """
        # Forward edge
        forward_edge = [v, capacity, 0]  # [to, capacity, flow]
        # Reverse edge for residual graph
        reverse_edge = [u, 0, 0]
        
        forward_edge.append(len(self.graph[v]))
        reverse_edge.append(len(self.graph[u]))
        
        self.graph[u].append(forward_edge)
        self.graph[v].append(reverse_edge)
    
    def _bfs(self, source: int, sink: int) -> List[int]:
        """
        Breadth-first search to construct level graph.
        
        :param source: Source vertex
        :param sink: Sink vertex
        :return: Level of each vertex or None if no augmenting path exists
        """
        # Reset level
        level = [-1] * self.num_vertices
        level[source] = 0
        
        # BFS queue
        queue = deque([source])
        
        while queue:
            u = queue.popleft()
            
            for i, (v, capacity, flow, _) in enumerate(self.graph[u]):
                # If not visited and residual capacity exists
                if level[v] == -1 and flow < capacity:
                    level[v] = level[u] + 1
                    queue.append(v)
        
        return level if level[sink] != -1 else None
    
    def _dfs(self, u: int, sink: int, flow: int, level: List[int], 
             flow_path: List[int]) -> int:
        """
        Depth-first search to find augmenting paths.
        
        :param u: Current vertex
        :param sink: Sink vertex
        :param flow: Current path flow
        :param level: Level graph
        :param flow_path: Current flow path
        :return: Augmented flow
        """
        # Reached sink
        if u == sink:
            return flow
        
        for i in range(flow_path[u], len(self.graph[u])):
            flow_path[u] = i
            
            edge = self.graph[u][i]
            v, capacity, current_flow, reverse_index = edge
            
            # Check level graph and residual capacity
            if (level[v] == level[u] + 1 and 
                current_flow < capacity):
                
                # Find bottleneck flow
                bottleneck = min(flow, capacity - current_flow)
                
                # Attempt to augment path
                temp_flow = self._dfs(v, sink, bottleneck, level, flow_path)
                
                if temp_flow > 0:
                    # Update forward and reverse edges
                    self.graph[u][i][2] += temp_flow
                    self.graph[v][reverse_index][2] -= temp_flow
                    
                    return temp_flow
        
        return 0
    
    def max_flow(self, source: int, sink: int) -> int:
        """
        Compute the maximum flow from source to sink.
        
        :param source: Source vertex
        :param sink: Sink vertex
        :return: Maximum flow value
        """
        # Validate input
        if source < 0 or source >= self.num_vertices or \
           sink < 0 or sink >= self.num_vertices or \
           source == sink:
            raise ValueError("Invalid source or sink")
        
        # Initialize max flow
        max_flow = 0
        
        # Dinic's algorithm main loop
        while True:
            # Construct level graph
            level = self._bfs(source, sink)
            
            # No augmenting path exists
            if level is None:
                break
            
            # DFS to find blocking flow
            flow_path = [0] * self.num_vertices
            while True:
                path_flow = self._dfs(source, sink, float('inf'), 
                                      level, flow_path)
                
                if path_flow == 0:
                    break
                
                max_flow += path_flow
        
        return max_flow