def solution(A):
    result = 0
    west = A.count(1)

    for cars in A:
        if cars == 0:
            result += west
            if result > 1e9:
                return -1
        else :
            west -=1

    return result




A = [0,1,0,1,1]
print(solution(A))
