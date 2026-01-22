# Adding a node in undirectional graph
def add_node(v):
    if v in graph:
        print(v, "is already present in the graph")
    else:
        graph[v] = []

# Adding an edge in undirectional graph with cost
def add_edge(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in graph")
    elif v2 not in graph:
        print(v2, "is not present in graph")
    else:
        list1 = (v2, cost)
        list2 = (v1, cost)
        graph[v1].append(list1)
        graph[v2].append(list2)

# Adding an edge in directional graph with cost
def add_edge_d(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in graph")
    elif v2 not in graph:
        print(v2, "is not present in graph")
    else:
        list1 = (v2, cost)
        graph[v1].append(list1)


graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("F")
add_edge("A", "B", 50)
add_edge("F", "C", 40)
add_edge("D", "F", 30)
add_edge_d("D", "F", 30)
add_edge_d("A", "D", 20)
add_edge_d("C", "A", 30)
print(graph)

