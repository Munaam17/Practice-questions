# Adding a node
def add_node(v):
    global node_count
    if v in nodes:
        print(v, "is already present in the graph")
    else:
        node_count += 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(1)
        graph.append(temp)

# for printing in adjacency matrix format

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j], end = " ")
        print()

nodes = []
graph = []
node_count = 0
add_node("A")
add_node("B")
add_node("C")
print(graph)
print()