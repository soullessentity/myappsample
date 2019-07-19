from collections import Counter
def occu_count(nums):
    nums1 = []
    for elm in range(0, len(nums)):
        if nums.count(nums[elm]) == 1:
            print(nums[elm])

def occu_count_unique(nums):
    cache = {}
    cache = Counter(nums)
    for key in cache:
        if cache[key] == 1:
            print(key)

    for i in range(0, len(nums)):
        if nums.count(nums[i]) == 1:
            print(nums[i])


if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 4, 7, 3, 5]
    # occurance_nums(numbers)
    occu_count(numbers)
    occu_count_unique(numbers)