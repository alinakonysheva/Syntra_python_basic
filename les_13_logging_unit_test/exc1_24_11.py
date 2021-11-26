
def get_unique_values(alist : list) -> list:
    newlist = []

    for item in alist:
        if item not in newlist:
            newlist.append(item)
    
    return newlist

if __name__ == '__main__':
    test = [1, 2, 3, 3, 4, 5]
    newlist = get_unique_values(test)
    print('{} -> {}'.format(test, newlist))