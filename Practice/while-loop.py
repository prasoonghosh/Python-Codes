x = 0
while x ** 2 <= 100:
    print(x ** 2)
    x += 1

def sum(x):
    s = 0
    while x > 0:
        d = x % 10
        x = x // 10
        s = s + d
    if s == 15:
        print(True)
    else:
        print(False)
sum(int(input("Enter num: ")))

def Break():
    x = 0
    while x < 3:
        x = x +1
        break
    print(x)
Break()