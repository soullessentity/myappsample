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
def find_elm_list(target):
    list1 = [1, 4, 5, 6, 7, 3, 8, 9]
    list1.sort()
    l = 0
    r = len(list)
    m =len(list)/2
    #c
    # for i in range(0, r):
    if list[m] > target:
        r = m-1
    elif list[m] < target:
        l = m+1
    elif list[m] == target:
        print(m)
    else:
        print("doesnt exists")




from heapq import merge
if __name__ == '__main__':
    join_list()
    find_elm_in_list(7)