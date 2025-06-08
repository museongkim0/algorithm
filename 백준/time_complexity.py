n = int(input())

A=[0]*n

# 알고리즘 수업 - 알고리즘의 수행 시간 1

# def MenOfPassion(A, n):
#     count = 1
#     complexity = 0
#     i = int(n / 2)
#     print(count)
#     print(complexity)
#     return A[i] # 코드1

def MenOfPassion(A, n):
    count = 0
    complexity = 0
    sum = 0
    for i in range(0, n):
        sum += A[i] # 코드1
        count += 1
    complexity += 1
    print(count)
    print(complexity)
    return sum

MenOfPassion(A, n)

