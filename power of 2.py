def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

num = int(input("Enter an integer: "))
if is_power_of_two(num):
    print("Output: True (It is a power of 2)")
else:
    print("Output: False (It is NOT a power of 2)")
