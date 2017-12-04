import sys

from order import order
from parse import parse_file

def main():
    filename = sys.argv[1]
    matrix = parse_file(filename)
    ordering = order(matrix)
    print(' '.join([str(x + 1) for x in ordering]))

if __name__ == '__main__':
    main()
