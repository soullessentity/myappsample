def convert_list_string(nums):
    result = ""
    for i in nums:
        result+= i
    print(result, type(result))

    result1 =" "
    print(result1.join(nums),type(result1))

def convert_string_list(str1):
    nums =[]
    for ch in str1:
        nums.append(ch)
    print(nums, type(nums))

def convert_string_int(tar):
    res = int(tar)
    print(res, type(res))

if __name__ == '__main__':
    numbers = ["hello" , "how", "are", "you"]
    string1 = "i am the tomorrow and forever"
    convert_list_string(numbers)
    convert_string_list(string1)
    convert_string_int("1234")