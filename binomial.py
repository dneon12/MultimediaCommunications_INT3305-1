import math

def prob(n, p, N):
    return combination(n, N)*(p ** n)*(1 - p)**(N - n)

def infoMeasure(n, p, N):
    return -math.log(prob(n, p, N), 2)

def sumProb(N, p):
    # Tong xac suat cac synbol n cua nguon thong tin binimial/ n: 1->N
    sum = 0 
    for i in range(1, N + 1):
        sum += prob(i, p, N)
    return sum

def approxEntropy(N, p):
    # entropy cua phan bo binomial
    sum = 0
    for i in range(1, N + 1):
        sum += prob(i, p, N)*infoMeasure(i, p, N)
    return sum

def factorial(n): #tinh giai thua 
    if n <= 1:
        return 1
    else:
        return n*factorial(n - 1)

def combination(i, N): #tinh to hop 
    return factorial(N)/(factorial(i)*factorial(N - i))