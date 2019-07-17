def threesum(nums, target):
    cache = {}
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if target - (nums[i] + nums[j]) in cache:
                print(cache[target -( nums[i] + nums[j])], i, j)
            else:
                cache[nums[i]] = i
                cache[nums[j]] = j

def threesum_i(nums,target):
    print("NEW LIFE")
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    print(i, j, k)


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    threesum(numbers,36)
    threesum_i(numbers,37)