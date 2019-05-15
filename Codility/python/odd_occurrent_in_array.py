def solution(A):
    x = 0
    for number in A:
        x = x^number
    return x


A = [9,3,9,3,9,7,9]
print(solution(A))
