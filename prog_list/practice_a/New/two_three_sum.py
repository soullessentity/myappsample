def two_sum(list1, target):
    cache = {}
    for i in range(0, len(list1)):
        if target - list1[i] in cache:
            print(cache[target - list1[i]],i)
        else:
            cache[list1[i]] = i

def three_sum(list1, target):
    cache = {}
    for i in range(0, len(list1)):
        for j in range(i+1, len(list1)):
            if target - (list1[i] +list1[j]) in cache:
                print(cache[target - (list1[i] +list1[j])],i,j)
            else:
                cache[list1[i]] = i
                cache[list1[j]] = j

if __name__ == '__main__':
    l1 = [ 1,3,4,5,6,2,7,8,9]
    two_sum(l1, 8)
    three_sum(l1, 9)