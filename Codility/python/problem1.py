def solution(N):
    str = ''
    for i in range (1,N+1):
        if i%2 == 1:
            str+='+'
        elif i%2 ==0:
            str+='-'
        else:
            return 1
    return str

N=4
print(solution(N))

