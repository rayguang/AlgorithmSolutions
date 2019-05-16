def solution(A):
    head = A[0]
    tail = sum(A[1:])
    diff = abs(tail-head)
    for k in A[1:-1]:
        head += k
        tail -= k
        diff = min(diff, abs(head-tail))
    return diff

A=[3,1,2,4,3]
print(solution(A))
