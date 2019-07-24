def reverse_s(str1):
    str2 = ""
    for ch in str1:
        str2 = ch + str2
    print(str2)

def substring_s(str1, sub):
    if str1.find(sub) == -1:
        print("False")
    else:
        print("True")

    sub = "like"
    if str.find(str1, sub) == -1:
        print("False")
    else:
        print("True")

def str_int(str1):
    val = int(str1)
    print(type(val))

def reverse_int(n):
    n1 = 0
    rev = 0
    print("ji")
    while n > 0:
        n1 = n%10
        rev = (rev *10) + n1
        n = n//10
    print(rev)

if __name__ == '__main__':
    reverse_s("hello")
    substring_s("hello", "he")
    str_int("1234")
    reverse_int(145)