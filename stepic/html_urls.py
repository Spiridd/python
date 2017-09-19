import requests
import re


def get_domains(url):
    domains = set()
    response = requests.get(url)
    text = response.text
    print(text)
    template_domain = re.compile(r'<a.*?href=["\'](?:\w+://)?(www\.)?([\w-]*\.?[\w-]*\.?[\w-]+\.\w+).*?["\']')
    for d in re.findall(template_domain, text):
        domains.add(d[0]+d[1])
    return domains


def main():
    url = input().rstrip()
    for d in sorted(list(get_domains(url))):
        print(d)


if __name__ == '__main__':
    main()
