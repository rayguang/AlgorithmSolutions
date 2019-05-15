def solution(A , K):
    # write your code in Python 3.6
    # 利用array相加做出rotation，A[-1]代表array的最後一個，依此類推。
    # more detail please check it out at https://openhome.cc/Gossip/CodeData/PythonTutorial/NumericString.html .
    if len(A) == 0:
        return A

    K =  K % len(A) 

    return A[-K:] + A[:-K]

# testcase 1 
A = [3, 8, 9, 7, 6]
K = 3
print(solution(A , K))

# testcase 2
A = [0, 0, 0]
K = 1
print(solution(A , K))

# testcase 3
A = [1, 2, 3, 4]
K = 4
print(solution(A , K))
