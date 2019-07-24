def string_rev(str1):
    str2 =""
    for ch in str1:
        str2 = ch + str2
    print(str2)
    print(str1[::-1])



if __name__ == '__main__':
    string_rev("hellohowdy")