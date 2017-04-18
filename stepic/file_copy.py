with open('data.txt', 'rt') as f, open('out.txt', 'wt') as out:
    strings = f.read().splitlines()
    for str in reversed(strings):
        out.write(str + '\n')
