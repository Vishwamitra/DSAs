# Famous Dijkstra's Algorithm - To derive shortest path

Dijkstra's algorithm is a popular algorithm used to find the shortest path between nodes in a graph. It works by starting at a designated source node and iteratively visiting neighboring nodes while keeping track of the distance from the source node. The algorithm uses a priority queue to visit the nodes in the order of their distance from the source node, ensuring that the algorithm always considers the closest unvisited node. Dijkstra's algorithm is widely used in various applications such as network routing, GPS navigation, and pathfinding in video games.

## Implementation of Dijkstra's Algorithm in Python
Here Dijkstra's algorithm is implemented using '''minHeap Data Structure''' in Python. Dijkstra's algorithm can be implemented using simple "array" data structure too but that will not be efficient. Implementation using minHeap is the most efficient way.