# 전체 tc
T= int(input())

numbers=["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(T):
    input()
    input_nums=input().split(' ')

    counts=[0]*10

    for input_num in input_nums:
        for i in range(10):
            if input_num==numbers[i]:
                counts[i] += 1
                break

    print('#{}'.format(tc+1))
    for i in range(10):
        for j in range(counts[i]):
            print(numbers[i], end=' ')
    print()