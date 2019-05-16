"""
Task:PermMissingElem
Find the missing element in a given permutation.
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
Your goal is to find that missing element.
Write a function:
def solution(A)
that, given an array A, returns the value of the missing element.
For example, given array A such that:
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.
You can check it out the result at https://app.codility.com/demo/results/training6B4P3V-QXJ/ .
"""

"""
Logic: members in the list are continuous from 1 to N+1, list index ranges from 0 to N. XOR index with each list member to find out which one is missing. Because index starts from 0, we need to XOR one additional element N+1
    
"""

def solution(A):
    result = len(A)+1
    for N in range(0,len(A)):
        result ^=(N+1)^A[N]
        print("N: {}  A[N]: {} result: {}".format(N, A[N], result))

    return result

A=[2,1,3,5]
print(solution(A))
