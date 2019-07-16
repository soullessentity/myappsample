def join_list():
    l1 = [3,6,1,2]
    l2 = [8,4,7,0]
    res = sorted(l1+ l2)
    print(res)

    res1 = list(merge(l1,l2))
    # res1.sort()
    print(res1)

    res3 = l1 + l2
    res3.sort()
    print(res3)

from heapq import merge
if __name__ == '__main__':
    join_list()