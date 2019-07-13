def convert_string_to_list():
    str1 = "geeks are here and lets kill then"
    #use list function
    num1 = list(str1)
    print(num1)
    num2 = []

    #actually extract character by characted and use append
    for ch in str1:
        num2.append(ch)
    print("num2", num2)

    #use string list and split fucntion to give space or fill list with agrument suggested
    num = list(str1.split(" "))
    print(num)

def convert_list_to_string():
    list = ["Hi", "hello", "how", "what", "when", "where"]
    str = ""
    # str = string(list)
    for element in list:
        str += element
    print(str)

    list1 = ["one", "two", "three", "four"]
    str1 = " "
    print(str1.join(list1))

from collections import Counter
def counter_charin_string():
    string1 = "hello i am divya"
    cache ={}
    j = 0
    for ch in string1:
        cache[ch] = string1.count(ch)
    print(cache)

    cache1 = {}
    for key in cache.keys():
        if cache[key] > 1:
            cache1[key]=cache[key]
    print(cache1)

    chach2 = {}
    cache2 = Counter(string1)
    print(cache2)

if __name__ == '__main__':
    convert_string_to_list()
    convert_list_to_string()
    counter_charin_string()