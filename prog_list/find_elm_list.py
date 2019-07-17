def find_element(list1, target):
    found = False
    for i in range(0, len(list1)):
        if list1[i] == target:
            print(i)
            found = True
            return found
        else:
            found = False
    return found

from heapq import merge
def combine_list(n1, n2):
    n3 = n1 + n2
    print(n3)

    n4 = list(merge(n1, n2))
    print("Hi",n4)

if __name__ == '__main__':
    numbers = [1,2,3,4,5,6]
    numbers1 = [7,8,9,10]
    print(find_element(numbers,6))
    combine_list(numbers,numbers1)
