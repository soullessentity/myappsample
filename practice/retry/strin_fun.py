def string_to_list(str1):
    list = []
    for ch in str1:
        list.append(ch)
    print(list)




from collections import Counter
def count_string_ch(str1):
    cache = {}
    cache = Counter(str1)
    print(cache)

    cas = {}
    for ch in str1:
        cas[ch] = str1.count(ch)
    print(cas)

    c2 ={}
    for key in cache.keys():
        if cache[key] > 1:
            c2[key] = cache[key]
    print(c2)

    cass = {}
    for ch in str1:
        if ch in cass:
            cass[ch]+=1
        else:
            cass[ch] =1
    print(cass)

if __name__ == '__main__':
    string_parse = "hello my name is udupi"
    string_to_list(string_parse)
    count_string_ch(string_parse)
