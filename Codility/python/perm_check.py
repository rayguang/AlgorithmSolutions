def solution(A):
    if set(A) == set( range(1, 1+len(A) ) ):
        return  1
    else:
        return 0

A=[4,1,3,2]
print(solution(A))
