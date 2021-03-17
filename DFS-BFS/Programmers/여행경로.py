# 1.{시작점 : [도착점들]} 쌍의 딕셔너리를 만들어줌
# 2. 도착점들을 역정렬 시켜준다
# 3. dfs 알고리즘을 통해 모든 점을 순회한다
#   3-1.첫번째로 문제 조건에 따라 ICN를 stack에 넣어줌
#   3-2.만약 top이 딕셔너리에 없거나(여행지의 맨 종착지라 없음), top을 시작점으로 하는 티켓이 없는 경우, 스택에서 꺼내와 path에 저장한다.
#   3-3. 경로가 존재하면 top을 시작점으로 하는 끝점 중 가장 알파벳 순으로 빨리오는(가장 마지막 지점)을 꺼내와 스택에 저장
# 4. 종료된 순서대로 path에 들어가 있으므로 path의 역순으로 답을 return 해준다
# https://gurumee92.tistory.com/165 예시 참고
# 예) 
# "ICN" -> "BOO"
# "ICN" -> "COO"
# "COO" -> "ICN"
# 1.
# path = []
# st = ["ICN"]
# route = {
# ICN : ["COO","BOO"]
# COO : ["ICN"]
# }
# 2.
# path = []
# st = ["ICN","BOO"]
# route = {
# ICN : ["COO"]
# COO : ["ICN"]
# }
# 3. 
# path = ["BOO"]
# st = ["ICN"]
# route = {
# ICN : ["COO"]
# COO : ["ICN"]
# }
# 4.
# path = ["BOO"]
# st = ["ICN","COO"]
# route = {
# ICN : []
# COO : ["ICN"]
# }
# 5.
# path = ["BOO"]
# st = ["ICN","COO","ICN"]
# route = {
# ICN : []
# COO : []
# }
# 6.
# path = ["BOO","ICN"]
# st = ["ICN","COO"]
# route = {
# ICN : []
# COO : []
# }
# 7.
# path = ["BOO","ICN","COO"]
# st = ["ICN"]
# route = {
# ICN : []
# COO : []
# }
# 8.
# path = ["BOO","ICN","COO","ICN"]
# st = []
# route = {
# ICN : []
# COO : []
# }
# answer = path[::-1]
def solution(tickets):
    routes = dict()
    for (start,end) in tickets:
        routes[start] = routes.get(start,[]) + [end]

    for r in routes.keys():
        routes[r].sort(reverse = True)

    stack = ["ICN"]
    path = []

    while stack:
        top  = stack[-1]
        # 맨 마지막 경로일경우 
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    answer = path[::-1]
    return answer

    
   