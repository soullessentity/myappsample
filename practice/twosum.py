def twosum(list, target):
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == target:
                print(f'[{i}], [{j}] :: {list[i]} + {list[j]} = {target}')


def twosum_o(list, target):
    cache = {}
    for i in range(0, len(list)):
        if target - list[i] in cache:
            print(cache[target - list[i]], i)
        else:
            cache[list[i]] = i


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6, 7 , 8, 9]
    twosum(list1, 7)
    twosum_o(list1, 7)
