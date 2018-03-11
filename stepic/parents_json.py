# inefficient algorithm
# add if ancestors[s]...
# else do what is written now
# # but works =)
# don't use union as 'abc' converts to ['a', 'b', 'c']
import json


def get_ancestors(name, parents):
    straight = set(parents[name])
    all_parents = set(straight)
    for s in straight:
        # all_parents = all_parents.union(get_ancestors(s, parents))
        for p in get_ancestors(s, parents):
            all_parents.add(p)
    # return all_parents.union(name)
    all_parents.add(name)
    return all_parents


def get_childs_count(name, ancestors):
    count = 0
    for class_name, class_ancestors in ancestors.items():
        if name in class_ancestors:
            count += 1
    return count


def main():
    classes_json = json.loads(input())

    parents = {}
    for record in classes_json:
        name = record['name']
        straight_parents = record['parents']
        parents[name] = straight_parents
    print(parents)

    ancestors = {}
    for name in parents:
        ancestors[name] = get_ancestors(name, parents)
    print(ancestors)

    list_ancestors = list(ancestors.items())
    list_ancestors.sort(key=lambda x: x[0])

    for one in list_ancestors:
        name = one[0]
        print('{} : {}'.format(name, get_childs_count(name, ancestors)))


if __name__ == '__main__':
    main()
