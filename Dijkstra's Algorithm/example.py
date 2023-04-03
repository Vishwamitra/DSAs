from dijkstra import Dijkstra

connections = {
    "AMS": {"BOM": 3, "DEL": 4, "GOP": 1},
    "BOM": {"GOP": 5, "DEL": 1},
    "DEL": {"GOP": 3},
    "GOP": {"DEL": 2},
}
startCity = "AMS"
# using heap data structure
distances = Dijkstra(connections, startCity, "heap")
print(distances.distances)

# using array data structure
distances = Dijkstra(connections, startCity, "array")
print(distances.distances)
