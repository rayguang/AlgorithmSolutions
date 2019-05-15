def solution(N):
    print("N binary: {} ".format(N,'b').strip('0').split('1'))
    return len(max((format(N,'b').strip('0').split('1'))))

N=20 
print ("{} binarygap is: {}".format(N,solution(N)))
