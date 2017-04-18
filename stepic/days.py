import datetime


year, month, day = map(int, input().split())
days = int(input())
now = datetime.date(year=year, month=month, day=day)
then = now + datetime.timedelta(days=days)
print(' '.join(map(str, [then.year, then.month, then.day])))
