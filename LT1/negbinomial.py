import math

def prob(n, p, r):
    return combination(n - r + 1, n)*(p ** n)*(1 - p)**r

def infoMeasure(n, p, r):
    return -math.log(prob(n, p, r), 2)

def sumProb(N, p, r):
    # Tong xac suat cac synbol n cua nguon thong tin negbinomial/ n: 1->N
    sum = 0 
    for i in range(1, N + 1):
        sum += prob(i, p, r)
    return sum

def approxEntropy(N, p, r):
     # entropy cua phan bo negbinomial
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p, r)*infoMeasure(i, p, r)
    return sum

def factorial(n): #tinh giai thua 
    if n <= 1:
        return 1
    else:
        return n*factorial(n - 1)

def combination(i, N): #tinh to hop 
    return factorial(N)/(factorial(i)*factorial(N - i))