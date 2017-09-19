def find(text, pattern):
    # TODO: choose bigger prime
    prime = 3
    size = len(pattern)
    # TODO: modular arithmetics
    leading = prime ** (size-1)
    p_hash = 0
    for char in reversed(pattern[1:]):
        p_hash += ord(char)
        p_hash *= prime
    p_hash += ord(pattern[0])
    t_hashes = [0] * (1+len(text)-size)
    for char in reversed(text[1-size:]):
        t_hashes[-1] += ord(char)
        t_hashes[-1] *= prime
    t_hashes[-1] += ord(text[-size])
    for index, char in reversed(tuple(enumerate(text[:-size]))):
        t_hashes[index] = t_hashes[index+1] - ord(text[index+size])*leading
        t_hashes[index] *= prime
        t_hashes[index] += ord(char)
    occurrences = []
    for index, h in enumerate(t_hashes):
        if h == p_hash and pattern == text[index:index+size]:
            occurrences.append(index)
    return occurrences


def main():
    pattern = input()
    text = input()
    occurrences = find(text, pattern)
    [print(o, end=' ') for o in occurrences]


if __name__ == '__main__':
    main()
