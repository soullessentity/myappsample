def reverse_lst(n):
    start = 0
    end = len(n)-1
    middle = (start + end)/2
    n.reverse()
    print(n)

    while(start <= end):
        n1 =[]
        i = 0

        temp = n[start]
        n[start] = n[end]
        n[end] = temp
        start+=1
        end-=1
    print(n)

if __name__ == '__main__':
    nums = [1,6,7,8,9,3,4]
    print(nums[::-1])
    # reverse_lst(nums)