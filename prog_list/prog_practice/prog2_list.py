def sub_lists(l1,l2):
    l1.reverse()
    print(l1)
    l1.sort()
    print(l1)
    l1.append(l2)
    print(l1)


if __name__ == '__main__':
    n = [1, 2, 3, 5, 6, 7, 4, 8, 9, 0, 11, 34, 13, 55, 26, 19, 42]
    n1 = [78, 34, 99, 63, 0, 87, 45, 13, 2]
    sub_lists(n,n1)