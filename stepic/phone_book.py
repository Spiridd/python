def main():
    max_size = int(1e7-1)
    book = [None] * max_size
    n = int(input())
    for _ in range(n):
        query = input().split()
        command = query[0]
        number = int(query[1])
        if command == 'add':
            book[number] = query[2]
        elif command == 'del':
            book[number] = None
        else:
            print(book[number] if book[number] else 'not found')


if __name__ == '__main__':
    main()
