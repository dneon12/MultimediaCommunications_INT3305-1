import math

def prob(n, p):
    return ((1 - p)**(n - 1))*p

def infoMeasure(n, p):
    return -math.log(prob(n, p), 2)

def sumProb(N, p):
    """
    De kiem chung tong xac suat cua phan bo geometric = 1, ta cho N = 99999999 và p = 0.5 de mo phong.
    In ra ket qua de thay duoc gia tri dung cua ham sumProb 
    """
    sum = 0 
    for i in range(1, N + 1):
        sum += prob(i, p)
    return sum

def approxEntropy(N, p):
    
   # Entropy la gia tri trung binh cua nguon tin -> se tinh duoc entropy cua nguon tin geometric. 
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p)*infoMeasure(i, p)
    return sum