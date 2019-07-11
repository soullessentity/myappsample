def two_sum(list,target):
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if list[i] + list[j] == target:
                print(f'[ {i}] , [{j}]')

def two_sum_optimal(list, target):
    cache = {}
    i =0
    for i in range(0,len(list)):
        if target - list[i] in cache:
            print(cache[target - list[i]], i)
        else:
            cache[list[i]] = i

if __name__ == '__main__':
    list = [3,5,7,8,9,2,4,1]
    two_sum(list, 11)
    two_sum_optimal(list, 11)