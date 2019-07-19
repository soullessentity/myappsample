def find_sub_string(full_string,sub):
    value = str.find(full_string,sub)
    if value == -1:
        print("False, sub string not present")
    else:
        print("True, sub string found")

    if full_string.find(sub) == -1:
        print("False")
    else:
        print("True")

if __name__ == '__main__':
    string1 = "anoohya mrudula kaayeschu"
    substr = "anoo"
    find_sub_string(string1,substr)