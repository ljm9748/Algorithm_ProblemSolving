def infix(root):    # 중위순회
    if tree[root][0] != -1:
        infix(tree[root][0])
    print(word[root],end='')
    if tree[root][1] != -1:
        infix(tree[root][1])

for tc in range(10):
    V=int(input())

    tree=[[-1,-1] for _ in range(V+1)]  # 노드관계
    word=['']*(V+1)                     # 알파벳 저장

    for i in range(V):
        input_list=list(input().split())
        word[int(input_list[0])]=input_list[1]
        if len(input_list)>=3:      # 만약 자식이 있다면
            for j in range(2,len(input_list)):
                if tree[int(input_list[0])][0] == -1:
                    tree[int(input_list[0])][0] = int(input_list[j])
                else:
                    tree[int(input_list[0])][1] = int(input_list[j])
    # 순회하며 출력
    print('#{} '.format(tc+1),end='')
    infix(1)
    print()