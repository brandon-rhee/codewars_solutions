def solution(number):
    if number <= 0:
        result = 0

    comb = []
    for i in range(1,number):
        if i%3 == 0:
            comb.append(i)
        elif i%5 ==0:
            comb.append(i)
    total = sum(comb)
    return total

print(solution(5))