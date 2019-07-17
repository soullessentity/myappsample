def two_sum(list, target):
    cache ={}
    for i in range(0, len(list)):
        if target - list[i] in cache:
            print(cache[target - list[i]], i)
        else:
            cache[list[i]] = i
if __name__ == '__main__':
    list1 = [1,4,2,5,3,6,9,0,8,7]
    two_sum(list1, 9)

