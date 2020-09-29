some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']


def find_dupe(alist):
    placeholder = []
    for a in alist:
        for b in alist:
            if a == b:
                placeholder.append(b)
            else:
                pass
    return placeholder

print(find_dupe(some_list))
