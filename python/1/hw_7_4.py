def collatz(n):

    cnt = 0

    while cnt < 500:

        #역시 n이 1이 들어올수도 있는데 그걸 생각 못한 디테일 부족
        #왜 실수 많이했지..?

        if n == 1:

            return cnt

        if n % 2 == 0:

            n = n // 2

        else:

            n = (n * 3) + 1
        
        cnt += 1
    
    return -1

print(collatz(6))

print(collatz(25))

print(collatz(54))

print(collatz(687))

print(collatz(1))
print(collatz(626331))
