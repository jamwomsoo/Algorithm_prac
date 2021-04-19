import sys
import math

class Node:
    def __init__(self,data):
        self.data = data
        self.child = [None for _ in range(10)]
        # 해당 노드를 마지막으로 끝나는 문자열이 있는지
        self.check = False
class Trie:
    def __init__(self):
        self.root = Node('')

    def insert(self,phone):
        tmp = self.root
        for i in phone:
   
            # 만약 child가 비어있지 않다면 child 노드로 이동
            if tmp.child[i] != None:
                tmp = tmp.child[i]
            # child가 비어있다면 새로운 자식 노드를 만들고 그 자식노드로 이동
            else:
                new = Node(i)
                tmp.child[i] = new
                tmp = new
        # 911-> 1에서 check가 True 됨
        tmp.check = True

    def consistency(self, phone):
        tmp = self.root
        for i in range(len(phone)):
            # 다른 문자열을 포함하고 있다면
            if tmp.check:
                return False
            tmp = tmp.child[phone[i]]
        return True
for _ in range(int(input())):
    n = int(input())
    phone_list = []
    trie = Trie()

    for _ in range(n):
        phone = list(map(int,input()))
       
        trie.insert(phone)
        phone_list.append(phone)
    result = True

    for p in phone_list:
        result *= trie.consistency(p)

    if result:
        print("YES")
    else:
        print("NO")