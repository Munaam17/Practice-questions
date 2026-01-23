# Adding a node in undirectional graph
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
            temp.append(0)
        graph.append(temp)

# Adding an edge in undirectional graph and with cost

def add_edge(v1, v2, cost):
    if v1 not in nodes:
        print(v1, "is not present in graph")
    elif v2 not in nodes:
        print(v1, "is not present in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph [index1][index2] = cost
        graph [index2][index1] = cost

        print(index1), print(index2)

# Adding an edge in directional graph and with cost

def add_edge_d(v1, v2, cost):
    if v1 not in nodes:
        print(v1, "is not present in graph")
    elif v2 not in nodes:
        print(v1, "is not present in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph [index1][index2] = cost

        print(index1), print(index2)

# for deleting the node in undirected, undirected from AM

def del_node(v):
    global node_count
    if v not in nodes:
        print(v,"is not present in nodes")
    else:
        index1 = nodes.index(v)
        node_count -= 1
        nodes.pop(index1)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)

# for deleting the node in directed for AM

def del_edgd(v1, v2):
    if v1 not in nodes:
        print(v1, "is not present in graph")
    elif v2 not in nodes:
        print(v1, "is not present in graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph [index1][index2] = 0
        # graph [index2][index1] = 0


# for printing in adjacency matrix format

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j], "<3"), end = " ")
        print()
# matrix = [[graph[i][j] for i in range(node_count)] for j in range(node_count)]


nodes = []
graph = []
node_count = 0

print(graph)
print(nodes)
print('Before adding the nodes')
add_node("A")
add_node("B")
add_node("C")
add_edge("A", "B", 90)
add_edge("B", "C", 80)
add_edge_d("A", "C", 70)
add_edge_d("B", "A", 60)
print("Nodes:",nodes)
print('Graph:',graph)
print_graph()
del_node("B")
del_edgd("A", "C")
# print(matrix1)
print('After adding the nodes')
print("Nodes:",nodes)
print('Graph:',graph)

print_graph()