def random_lists(l1,l2):
    l1.reverse()
    print(l1)
    l1.sort()
    print(l1)
    l1.append(l2)
    print(l1)
    l1 = l1 + l2
    print(l1)

import itertools
def sub_list_inbuilt(l1):
    for i in range(0, len(l1)+1):
        l2 = (list(itertools.combinations(l1,i)))
        print(l2)


def sub_set_list(l1):
    sub_set = [[]]
    for i in range(len(l1)+1):
        for j in range(i+1,len(l1)+1):
            sub = l1[i:j]
            sub_set.append(sub)
    print(sub_set)

def largest_sum_list(l1):
    l1.sort()
    print(l1)
    large = l1[len(l1)-1] + l1[len(l1)-2]
    print(large)

    
if __name__ == '__main__':
    n = [1, 2, 3, 5, 6, 7, 4, 8, 9, 0, 11, 34, 13, 55, 26, 19, 42]
    n1 = [78, 34, 99, 63, 0, 87, 45, 13, 2]
    n2 = [1,2,0]
    # random_lists(n,n1)
    sub_list_inbuilt(n2)
    # sub_set_list(n2)
    largest_sum_list(n1)