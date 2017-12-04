test = [[False, False, False, False, False],
 [False, False, True, False, True],
 [True, False, False, False, True],
 [False, False, True, False, False],
 [True, False, False, False, False]]

def order(matrix):
    num_nodes = len(matrix)
    visited = [False] * num_nodes
    ordered_nodes = []
    # will get next node one at a time
    for i in range(num_nodes):

        # find the node that doesn't need anything
        head_node = None
        for j in range(num_nodes):
            if not visited[j] and not any(matrix[j]):
                head_node = j
                break
        if head_node is None:
            return None

        ordered_nodes.append(head_node + 1)
        for i in range(num_nodes):
            matrix[i][j] = False

        visited[j] = True

    return ordered_nodes

print(order(test))


