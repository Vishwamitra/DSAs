import heapq


class Dijkstra:
    def __init__(self, connections, start, type="heap"):
        self.connections = connections
        self.start = start
        if type == "heap":
            self.distances = self.dijkstraUsingHeap()
        else:
            self.distances = self.dijkstraUsingArray()

    def dijkstraUsingHeap(self):
        """
        Dijkstra's algorithm using minHeap Data Strcuture

        Parameters:
        ---------------
            connections : nested dictionary with all possible connections and distances [weight]
            start       : starting city name [starting node]

        returns:
        ---------------
            returns a dictionary with shortest distances to reach each places from starting city

        """
        connections = self.connections
        start = self.start
        # first all distances to infinity in the disctionary
        distances = {connection: float("inf") for connection in connections}
        # distance from start to start point = 0
        distances[start] = 0
        minHeap = [(0, start)]

        # loop through until heap is empty
        # heap will be empty when all the cities are traversed
        # once which are reachable from starting city.

        while minHeap:
            current_distance, current_city = heapq.heappop(minHeap)
            # if min distance is already found - do nothing - continue
            if current_distance > (distances[current_city]):
                continue
            # else get the distances and find the minimum one
            for childCity, distance in connections[current_city].items():
                NewDistance = current_distance + distance
                if NewDistance < distances[childCity]:
                    distances[childCity] = NewDistance
                    heapq.heappush(minHeap, (NewDistance, childCity))
        return distances

    def dijkstraUsingArray(self):
        """
        Dijkstra's algorithm using array Data Strcuture

        Parameters:
        ---------------
            connections : nested dictionary with all possible connections and distances [weight]
            start       : starting city name [starting node]

        returns:
        ---------------
            returns a dictionary with shortest distances to reach each places from starting city

        """
        connections = self.connections
        start = self.start
        # first all distances to infinity in the disctionary
        distances = {connection: float("inf") for connection in connections}
        # distance from start to start point = 0
        distances[start] = 0
        visited = set()
        while len(visited) != len(connections):
            connection, minDistance = self.__getMinimumDistance(distances, visited)

            if minDistance == float("inf"):
                break
            visited.add(connection)
            for destination, distance in connections[connection].items():
                newDistance = minDistance + distance
                currentDistance = distances[destination]
                if currentDistance > newDistance:
                    distances[destination] = newDistance
        return distances

    def __getMinimumDistance(self, distances, visited):

        minDistance = float("inf")
        vertex = None
        for vertexId, distance in distances.items():
            if vertexId in visited:
                continue
            if distance <= minDistance:
                minDistance = distance
                vertex = vertexId
        return vertex, minDistance
