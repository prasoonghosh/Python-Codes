# WAP to print Fibonacci series the number of values to be printed should be taken as input from the user
# WAP to iterate a loop from 1 to 10. Implement the following conditions in the program
# (i)	When 6 is encountered, we want to break the loop and return to the outer condition.

n = int(input("Enter n: "))
i = 0
j = 1
while i <= n:
    print(i)
    series = i + j
    i = j
    j = series