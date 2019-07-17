def twosum(list, target):
    cache = {}
    for i in range(0,len(list)):
        if target - list[i] in cache:
            print(cache[target - list[i]], i)
        else:
            cache[list[i]] = i

def twosum_1(list, target):
    for i in range(0,len(list)):
        for j in range(i+1, len(list)):
            if list[i]+list[j] == target:
                print(f'[{i}], [{j}]')


if __name__ =='__main__':
    list = [1,13, 24, 23, 22, 21, 2, 3, 4,6, 7]
    twosum(list, 29)
    twosum_1(list, 29)
