from itertools import permutations

def read_grid_file(file_path):
    # Stations
    stations = []
    station_s = ()
    stations_b = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        grid_rows, grid_cols = map(int, lines[0].strip().split(','))

        for line in lines[1:]:
                data = line.strip().split(',')
                if len(data) == 3:
                    height,  x, y = map(int, data)
                    stations.append((height, x, y))
                if len(data) == 2 and station_s != ():
                    x, y = map(int, data)
                    stations_b.append((x, y))
                elif len(data) == 2:
                    x, y = map(int, data)
                    station_s = (x, y)

    return grid_rows, grid_cols, stations, station_s, stations_b

def time_between_stations(height1, height2):
    return max(-1, 1 + (height2 - height1))

def neighbors(x, y, grid_rows, grid_cols):
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < grid_rows and 0 <= ny < grid_cols:
            yield nx, ny

def BellmanFord(dist, src, graph):
    # Initialize distance from src to all other vertices
    dist[src] = 0

    # Relax all edges |V| - 1 times. Shortest path from src to any other vertex can have at-most |V| - 1 edges.
    for _ in range(len(dist) - 1):
        # Update dist value of adjacent vertices of the picked vertex.
        # Consider only those vertices which are still in queue
        for u, v, w in graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Negative weight cycles check
    for u, v, w in graph:
        if dist[u] != float("Inf") and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycle")
            return None

    return dist

def calculate_path_cost(path, graph):
    total_cost = 0
    for i in range(len(path) - 1):
        src = path[i]
        dest = path[i + 1]
        total_cost += BellmanFord(dist[:], src, graph)[dest]
    return total_cost

grid_rows, grid_cols, stations, station_s, stations_b = read_grid_file("grid.txt")
print("Grid Dimensions:", grid_rows, "rows,", grid_cols, "columns\n")

print("Station S:", station_s)
print("Stations B:", stations_b)
print('\n')

# Distances
num_vertices = grid_rows * grid_cols
dist = [float("inf")] * num_vertices

# Stations graph
graph = []
for i in range(grid_rows):
    for j in range(grid_cols):
        for ni, nj in neighbors(i, j, grid_rows, grid_cols):
            graph.append((i * grid_cols + j, ni * grid_cols + nj, time_between_stations(stations[i * grid_cols + j][0], stations[ni * grid_cols + nj][0])))

all_permutations = permutations(stations_b)

min_cost = float('inf')

for perm in all_permutations:
    # Calculate total cost of path for perm
    path = [station_s[1] * grid_cols + station_s[0]] + [y * grid_cols + x for x, y in perm]
    path_cost = calculate_path_cost(path, graph)
    
    min_cost = min(min_cost, path_cost)

print("Minimum cost of any supply path:", min_cost)

with open("pathLength.txt", "w") as file:
    file.write(str(min_cost))