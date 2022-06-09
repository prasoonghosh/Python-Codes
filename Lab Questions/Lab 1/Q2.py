# WAP to read an integer ‘n’ from STDIN. For all non-negative integers i<n, print i**2 on a separate line.

n = int(input("Enter the value of n: "))
for i in range(n):
    if n >=1:
        print(i**2)