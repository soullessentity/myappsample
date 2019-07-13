def three(list, target):
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            for k in range(j+1, len(list)):
                if list[i] + list[j]+list[k] == target:
                    print(f'[{i}], [{j}], [{k}] --> {list[i]} + {list[j]} + {list[k]} = {target}')

def three_o(list, target):
    cache = {}
    k = 0
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            k = target - (list[i] + list[j])
            if k in cache:
                if k != i and k != j and i != j :
                    print(cache[target - (list[i] + list[j])], i , j)
            else:
                cache[list[i]] = i
                cache[list[j]] = j


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6, 7 , 8, 9]
    three(list1, 7)
    three_o(list1, 7)