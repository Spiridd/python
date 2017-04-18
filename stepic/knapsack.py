# not finished
import sys


def main():
    reader = [tuple(map(int, line.split())) for line in sys.stdin]
    a, b = next(reader)
    c = list(reader)
    print(c)


if __name__ == '__main__':
    main()
