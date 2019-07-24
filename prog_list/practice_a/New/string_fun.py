def count_char(string1):
    cache  = {}
    count = 0
    for ch in string1:
        if ch in cache:
            cache[ch] += 1
        else:
            cache[ch] = 1
    print(cache)

    for key in cache.keys():
        has_dup = False
        if cache[key] >1:
            has_dup = True
            return has_dup
        else:
            has_dup = False
    return has_dup

def inbuilt_sount(string1):
    cache = {}
    for ch in string1:
        cache[ch] = string1.count(ch)
    print(cache)

    for ch in string1:
        if string1.count(ch) >1:
            print("duplicate exists")
            return True
        else:
            return False
def sub_string(s1, sub):
    val = str.find(s1, sub)
    if val == -1:
        print("substring not present")
    else:
        print("sub string  present")

def sub_string_1(s1, sub):
    val = s1.find(sub)
    if val == -1:
        print("substring not present")
    else:
        print("sub string  present")
if __name__ == '__main__':
    # has_dupl = count_char("Hello I am Wonderful")
    # if has_dupl == True:
    #     print("Duplicate present")
    # else:
    #     print("Duplicate not present")
    # Vale = inbuilt_sount("hello how are you ")
    #
    # if Vale == True:
    #     print("Duplicate present")
    # else:
    #     print("Duplicate not present")
    sub_string("hello, i am here" , "hel")
    sub_string_1("hello, i am here", "tata")