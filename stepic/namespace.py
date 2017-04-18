all_namespaces = {'global': {'parent': '', 'vars': []}}
n = int(input())
for _ in range(n):
    query = input().split()
    command = query[0]
    namespace = query[1]
    var_name = query[2]
    if command == 'create':
        all_namespaces[namespace] = {'parent': var_name, 'vars': []}
    elif command == 'add':
        try:
            all_namespaces[namespace]['vars'].append(var_name)
        except:
            print('no namespace named %s' % namespace)
    else:
        while True:
            if var_name in all_namespaces[namespace]['vars']:
                print(namespace)
                break
            else:
                namespace = all_namespaces[namespace]['parent']
                if not namespace:
                    print('None')
                    break
