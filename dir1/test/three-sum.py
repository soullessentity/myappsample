def three_sum(list, target):
    for i in range(0,len(list)):
        for j in range(i+1, len(list)):
            for k in range(j+1, len(list)):
                if list[i]+list[j]+list[k] == target:
                    print(f'[{i}], [{j}], [{k}] // {list[i]} + {list[j]} + {list[k]} ')

def three_sum_optimal(list, target):
    cache = {}
    i = 0
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if target - (list[i] + list[j]) in cache:
                print(cache[target - (list[i] + list[j])], i, j)
            else:
                cache[list[i]] = i
                cache[list[j]] = j

if __name__ == '__main__':
    list_1 = [1, 4, 6, 7, 8, 3, 9 , 5, 2, 10, 0, 11, 13]
    print(len(list_1))
    three_sum(list_1, 7)
    three_sum_optimal(list_1, 7)