from collections import Counter
def counter_duplicate1(string):
    cache = {}
    cache = Counter(string)
    print(cache)

def counter_duplicate2(string):
    cache ={}
    for ch in string:
        cache[ch] = string.count(ch)
    print(cache)

def counter_duplicate(string):
    cache = {}
    for ch in string:
        if ch in cache:
            cache[ch]+=1
        else:
            cache[ch]=1
    print(cache)

def has_duplicate(string):
    cache = {}
    has_dup = False
    for ch in string:
        if ch in cache:
            cache[ch] += 1
        else:
            cache[ch] = 1
    print(cache)

    for key in cache.keys():
        if cache[key] > 1:
            has_dup = True
            return has_dup
        else:
            has_dup = False

    return has_dup


if __name__ == '__main__':
    string1 = "ugyretyyyft juuhttrtrr khisty"
    counter_duplicate(string1)
    counter_duplicate1(string1)
    counter_duplicate2(string1)
    print(has_duplicate(string1))


