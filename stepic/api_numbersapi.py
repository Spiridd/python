import requests


def get_api_url(number):
    return ''.join(['http://numbersapi.com/', str(number), '/math?json=true'])


def isintresting(number):
    url = get_api_url(number)
    response = requests.get(url)
    json_text = response.json()
    return json_text['found']


def main():
    with open('numbers.txt', 'rt') as f:
        for line in f:
            n = int(line)
            if isintresting(n):
                print('Interesting')
            else:
                print('Boring')


if __name__ == '__main__':
    main()
