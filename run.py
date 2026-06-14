# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

print("Búsqueda en Anchura: ")
print(search.breadth_first_graph_search(ab).path())
print("Búsqueda en Profundidad: ")
print(search.depth_first_graph_search(ab).path())

print("Branch and Bound: ")
print(search.branch_and_bound(ab).path())
print("Branch and Bound con subestimación: ")
print(search.branch_and_bound_underestimation(ab).path())