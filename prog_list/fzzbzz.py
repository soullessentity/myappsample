def fizzbuzz(target):
    for i in range(0,target+1):
        if i%7 == 0:
            print("cuzz")
        else:
            if i%3 == 0 and i%5 == 0:
                print("fizzbuzz")
            elif i%3==0 and i%5 !=0:
                print("fizz")
            elif i%3!=0 and i%5==0:
                print("buzz")
            else:
                print(i)

if __name__ == '__main__':
    fizzbuzz(35)