def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(x):
    current = x + 1
    while True:
        if is_prime(current):
            return current
        current += 1

num = int(input("Enter a number X: "))
result = next_prime(num)
print(f"The smallest prime number greater than {num} is: {result}")
