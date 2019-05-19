def solution(X, A):
    n = [-1]*(X+1)
    for idx, v in enumerate(A):
        if n[v] == -1:
            n[v] = idx
        else:
            continue
    if -1 not in n[1:]:
        return max(set(n))
    else:
        return -1

A=[1,3,1,4,2,3,5]
print(solution(5, A))
