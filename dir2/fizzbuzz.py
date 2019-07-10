def fizzbuzz(number):
    i = 0
    for i in range(0, number+1):
        if i%2 == 1:
            if i%3 == 0 and i%5 == 0:
                print(i,"fizzbuzz")
            elif i%5 == 0 and i%3 != 0:
                print(i, "fizz")
            elif i%3 == 0 and i%5 != 0:
                print(i , "buzz")
            else:
                print(i)
if __name__ == '__main__':
    fizzbuzz(45)
