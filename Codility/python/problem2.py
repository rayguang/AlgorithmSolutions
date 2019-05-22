def solution(S, K):
    # write your code in Python 3.6
    day_dict = {0:'Mon', 1:'Tue', 2:'Wed', 3:'Thu', 4:'Fri', 5:'Sat', 6:'Sun'}
    return day_dict[list(day_dict.values()).index(S)+K]


S='Wed'
K=2
print(solution(S,K))
