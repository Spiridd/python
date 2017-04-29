import requests
import re


def get_urls(url):
    response = requests.get(url)
    text = response.text
    template_url = re.compile(r'<a.*?href="(.*?)"')
    urls = re.findall(template_url, text)
    return urls


def cross_pass(u1, u2):
    for u in get_urls(u1):
        urls = get_urls(u)
        if u2 in urls:
            return True
    return False


def main():
    url1 = input()
    url2 = input()
    if cross_pass(url1, url2):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
