def solution(N,A):
    result = [0] * N
    max_to_set = 0
    current_max = 0
    for i in A:
        print("i: {}  max_to_set: {}  current_max: {}".format(i, max_to_set, current_max))
        print("before:", result)
        if 1 <= i <= N:
            if result[i - 1] < max_to_set:
                result[i-1] = max_to_set
            result[i-1] +=1

            if current_max < result[i-1]:
                current_max = result[i-1]
            
        else:
            max_to_set = current_max
        print("after:", result)
    result = [max(max_to_set, i)for i in result]
    return result




N=5
A=[3,4,4,6,1,4,4]
print(solution(N,A))
