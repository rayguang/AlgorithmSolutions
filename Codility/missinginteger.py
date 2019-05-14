def solution(A):
    A.sort()
    min=1
    for i in A:
        if i > min:
            return min
        if i > 0:
            min = i
    return min


a= [2, 3, 7, 6, 8, -1, -10, 15]
print("solution for list {}".format(a))
print("solution: {}".format(solution(a)))
