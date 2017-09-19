from xml.etree import ElementTree


def parse_cubes(root, colors, value):
    colors[root.attrib['color']] += value
    value += 1
    for child in root:
        parse_cubes(child, colors, value)


def main():
    root = ElementTree.fromstring(input())
    colors = {'red': 0, 'green': 0, 'blue': 0}
    starting_value = 1
    parse_cubes(root, colors, starting_value)
    print(colors['red'], colors['green'], colors['blue'])


if __name__ == '__main__':
    main()
