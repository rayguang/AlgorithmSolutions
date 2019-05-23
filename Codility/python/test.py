def solution(L):
    newset=set()
    l=[]
    print(newset)
    for i in L:
        if i not in newset:
            l.append(i)
            newset.add(i)
    return l

l=[2,2,1,3,3,4,5,6,7,7]
print(solution(l))