def solution(A):
    K = 1
    for K in range(1, len(A)):
        temp = abs(sum(A[:K]) - sum(A[K:]))
        if K == 1:
            min = temp
        print('A[:K]: {}  A[K:]:  {}  temp: {}'.format(A[:K], A[K:], temp))
        if (temp < min):
            min = temp

    return min

A=[3,1,2,4,3]
print(solution(A))
