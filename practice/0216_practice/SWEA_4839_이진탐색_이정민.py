def findhalf(l,r):
    return (l+r)//2
# 전체 tc개수
T=int(input())

# 전체 tc만큼 반복
for tc in range(T):
    # 각 tc별 P, A, B
    P,A,B=map(int, input().split())

    # 초기화
    min_a=min_b=1   # 알게된 최소
    max_a=max_b=P   # 알게된 최대

    while min_a<max_a and min_b<max_b:
        tmp_a = findhalf(min_a, max_a)
        tmp_b = findhalf(min_b, max_b)
        # 정답자 판별
        if tmp_a == A and tmp_b == B:
            print('#{} {}'.format(tc+1, 0))
            break
        elif tmp_a == A:
            print('#{} A'.format(tc+1))
            break
        elif tmp_b == B:
            print('#{} B'.format(tc+1))
            break

        # 아무도 못맞춘 경우
        else:
            if A>tmp_a:
                min_a=tmp_a
            else:
                max_a=tmp_a
            if B>tmp_b:
                min_b=tmp_b
            else:
                max_b=tmp_b

# tc 5 5 5의 경우??
