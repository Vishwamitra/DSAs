import heapq

def dijkstraAlgorithm(connections, start):
    '''
    Dijkstra's algorithm using minHeap Data Strcuture
    
    Parameters:
    ---------------
        connections : nested dictionary with all possible connections and distances [weight]
        start       : starting city name [starting node]
        
    returns:
    ---------------
        returns a dictionary with shortest distances to reach each places from starting city
        
    '''
    
    # first all distances to infinity in the disctionary
    distances = { connection: float('inf') for connection in connections}
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


if __name__ == "__main__":
    connections = {'AMS': {'BOM': 3, 'DEL': 4, "GOP": 1}, 'BOM': {'GOP': 5, 'DEL':1}, 'DEL': {'GOP': 3}, 'GOP': {"DEL" : 2}}
    startCity= 'AMS'
    print(dijkstraAlgorithm(connections, startCity))