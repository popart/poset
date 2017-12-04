"""
    Return an ordering of a partially ordered set,
    where the set orderings are represented by links in an adjacency matrix
    and the set items are represented by an index in the matrix
"""
def order(matrix):
    num_nodes = len(matrix)
    visited = [False] * num_nodes
    ordered_nodes = []
    # get each head node (node w/o dependencies) one at a time
    for i in range(num_nodes):
        head_node = None
        # choose smallest (by index) node w/ no dependencies
        for j in range(num_nodes):
            if not visited[j] and not any(matrix[j]):
                head_node = j
                break

        # no head node means there is a cycle -> exit
        if head_node is None:
            raise Exception('Cycle detected in rules')

        ordered_nodes.append(head_node)

        # remove any dependencies to the head node
        # (so that there will be a new head node)
        for k in range(num_nodes):
            matrix[k][j] = False

        visited[j] = True

    return ordered_nodes
