def solution(X,A):
    result = [0]*X
    max_to_set = 0
    current_max = 0

    for i in A:
        if 1 <= i <= X:
            if result[i-1] < max_to_set:
                result[i-1] = max_to_set

            result[i-1] += 1

            if result[i-1] > current_max:
                current_max  =  result[i-1]
                
        else:
            max_to_set = current_max
    result=[max(max_to_set,i) for i in result]
    return result

X=5
A=[3,4,4,6,1,4,4]
print(solution(X,A))
