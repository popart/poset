def order(matrix):
    num_nodes = len(matrix)
    visited = [False] * num_nodes
    ordered_nodes = []
    # will get the head node (node w/o dependencies) one at a time
    for i in range(num_nodes):
        head_node = None
        # deterministic order if multiple head nodes (choose smallest)
        for j in range(num_nodes):
            if not visited[j] and not any(matrix[j]):
                head_node = j
                break

        # no head node means there is a cycle -> exit
        if head_node is None:
            raise Exception('Cycle detected in rules')

        ordered_nodes.append(head_node + 1)  # node numbering starts w/ 1, not 0

        # remove any dependency links to head node
        # (so that there will be a new head node)
        for i in range(num_nodes):
            matrix[i][j] = False

        visited[j] = True

    return ordered_nodes
