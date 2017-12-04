def parse_file(filename):
    with open(filename, 'r') as f:
        header = f.readline()
        num_nodes = int(header[0])
        matrix = create_matrix(num_nodes)

        for line in f:
            node = int(line[0]) - 1
            req_nodes = [int(x) - 1 for x in line[4:].split(' ')]
            for n in req_nodes:
                matrix[node][n] = True

        return matrix

def create_matrix(num_nodes):
    return [[False for _ in range(num_nodes)] for _ in range(num_nodes)]
