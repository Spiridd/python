import simplecrypt


with open('encrypted.bin', 'rb') as f:
    encrypted = f.read()
passwords = []
with open('passwords.txt', 'rt') as f:
    passwords.extend(f.read().splitlines())
print(passwords)
for p in passwords:
    try:
        decrypted = simplecrypt.decrypt(p, encrypted).decode('utf-8')
        print(decrypted)
    except simplecrypt.DecryptionException:
        pass
