import socket


def main():
    request = 'close'.encode()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 1234))
    s.send(request)
    response = s.recv(1024)
    print('response:', response.decode())
    s.close()


if __name__ == '__main__':
    main()

