def prim(x):
    if x < 2:
        return False
    elif x%2 == 0 and x != 2:
        return False
    else:
        i = 3
        while i*i <= x:
            if x%i == 0:
                return False
            i += 1
    return True

n = int(input('Enter a number n:'))
counter = 1
if n == 1:
    print(1)
else:
    for i in range(2, n+1):
        if prim(i):
            counter += 1
            if counter == n:
                print(i)
        else:
            for j in range(2, i):
                if i%j == 0 and prim(j):
                    counter += 1
                    if counter == n:
                        print(j)
        if counter >= n:
            break
