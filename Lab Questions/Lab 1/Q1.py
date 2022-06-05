# Given an integer n, perform the following conditional actions:
# ·      If n is odd, print Weird
# ·      If n is even and in the inclusive range of 2 to 5, print Not Weird
# ·      If n is even and in the inclusive range of 6 to 20, print Weird
# ·      If n is even and greater than 20, print Not Weird
def odd_even(number):
    if number%2 !=0:
        print("Weird")
    elif number%2 == 0 and 2 <= number <= 5:
        print("Not Weird")
    elif number%2 == 0 and 6 <= number <= 20:
        print("Weird")
    elif number%2 == 0 and number > 20:
        print("Not Weird")
odd_even(5)