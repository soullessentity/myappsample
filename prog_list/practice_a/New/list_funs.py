def sort_list(list1):
    list1.sort()
    print(list1)

def reverse_list(list1, list2):
    list2.reverse()
    print(list2)

    a = [1, 4, 6, 7]
    print(a[::-1])


def find_elm_list(list1, target):
    for elm in range(0, len(list1)):
        if list1[elm] == target:
            print(target, " element found in index ", elm)
            return True
        else:
            return False

from heapq import merge
def join_lists(l1, l2):
    l3 = []
    l3 = l1 + l2
    l3.sort()
    print(l3)

    l4 = []
    l4 = list(merge(l1,l2))
    print(l4)

from collections import Counter
def find_unq_elm(l2):
    cache = {}
    for ele in range(0, len(l2)):
        if l2.count(l2[ele]) == 1:
            print(l2[ele])

    cache = Counter(l2)

    for key in cache:
        if cache[key] == 1:
            print(key)


if __name__ == '__main__':
    list1 = [1, 5, 6, 8]
    list2 = [ 7, 6, 9, 3, 7, 5, 9, 1, 6, 5]
    sort_list(list1)
    find_elm_list(list2, 7)
    join_lists(list1, list2)
    reverse_list(list1, list2)
    find_unq_elm(list2)