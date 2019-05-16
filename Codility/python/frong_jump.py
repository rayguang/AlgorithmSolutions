def solution(X, Y, D):
    tail = 0
    if ((Y-X)%D!=0):
        tail = 1
    return (Y-X) // D + tail
