print('Input two integers')
n1 = int(input())
n2 = int(input())
P = True
fr1 = [0]*10
fr2 = [0]*10
while n1 > 9:
    fr1[int(n1%10)] = 1
    n1 /= 10
fr1[int(n1)] = 1
while n2 > 9:
    fr2[int(n2%10)] = 1
    n2 /= 10
fr2[int(n2)] = 1
for i in range(10):
    if fr1[i] != fr2[i]:
        P = False
if P:
    print('The numbers contain the same digits')
else:
    print('The numbers do not contain the same digits')
