s = input()
t = input()

count = 0
for i in range(len(s)-len(t)+1):
    probe = s[i:i+len(t)]
    if probe == t:
        count += 1
print(count)
