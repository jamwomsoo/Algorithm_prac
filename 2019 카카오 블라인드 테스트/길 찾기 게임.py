import sys
sys.setrecursionlimit(10**6)
# 파이썬 트리구조를 알고있냐 문제이다

class Tree:
    # 노드 생성시(생성자 역할)
    #             data
    #   left(none)   right(none) 이 생성됨
    def __init__(self,_list):
        self.data = max(_list,key = lambda x: x[1])
        # x 값보다 작은 값들만 왼쪽으로 뺀다
        left_list = list(filter(lambda x : x[0] < self.data[0], _list))
        # x 값보다 큰 값들만 오른쪽으로 뺀다
        right_list = list(filter(lambda x : x[0] > self.data[0], _list))
        
        # 왼쪽 노드
        # 만약 왼쪽리스트가 있으면 왼쪽 자식 서브 트리를 생성한다
        if left_list:
            self.left = Tree(left_list)
        # 없으면 맨 마지막에 None을 붙여줌
        else:
            self.left = None
        
        #오른쪽 노드
        # 만약 오른쪽리스트가 있으면 오른쪽 서브 트리를 생성한다
        if right_list:
            self.right = Tree(right_list)
        # 없으면 맨 마지막에 None을 붙여줌
        else:
            self.right = None

def fix(node, preList, postList):
    # 전위 순회
    preList.append(node.data)
    if node.left != None:
        fix(node.left, preList, postList)
    if node.right != None:
        fix(node.right, preList, postList)
    # 후위 순회
    postList.append(node.data)


def solution(nodeinfo):
    answer = []
    # 트리를 생성
    root = Tree(nodeinfo)
    
    postList = []
    preList = []
    # 전위, 후위를 구해주는 함수
    fix(root,preList,postList)
    # map을 통해 preList에 존재하는 좌표가 nodeinfo함수에서 몇번째 인덱스인지 구해준다
    answer.append(list(map(lambda x : nodeinfo.index(x)+1, preList)))
    answer.append(list(map(lambda x : nodeinfo.index(x)+1, postList)))
    
    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))