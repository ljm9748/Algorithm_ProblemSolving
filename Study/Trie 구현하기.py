class Node(object):
    def __init__(self, key, data=None):
        self.key=key        # 문자
        self.data=data      # 단말노드인 경우 문자저장
        self.children={}    # 자식노드

class Trie:
    # 트라이 초기화
    def __init__(self):
        self.head=Node(None)

    # 문자열 삽입
    def insert(self, string):
        current_node=self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data=string

    # 문자열 검색
    def search(self, string):
        current_node=self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False

        # 마지막까지 탐색했을때 그 단어가 단말노드면
        if current_node.data:
            return True
        else:
            return False
