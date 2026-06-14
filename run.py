# Search methods

import search

def show_solution(solution):

    path = list(reversed(solution.path()))
    states = [node.state for node in path]

    print("Ruta solución:", states)
    print("Coste total:", solution.path_cost)


ab = search.GPSProblem('A', 'B', search.romania)

print("Búsqueda en Anchura:")
show_solution(search.breadth_first_graph_search(ab))

print("\nBúsqueda en Profundidad:")
show_solution(search.depth_first_graph_search(ab))

print("\nBranch and Bound:")
show_solution(search.branch_and_bound(ab))

print("\nBranch and Bound con Subestimación:")
show_solution(search.branch_and_bound_underestimation(ab))