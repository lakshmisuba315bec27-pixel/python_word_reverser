import sys
try:
    n = int(raw_input("Input: "))
except NameError:
    n = int(input("Input: "))
print("0")
for i in range(1, n + 1):
    for x in range(n - i + 1, n + 1):
        sys.stdout.write(str(x))
    sys.stdout.write("0")
    for x in range(n, n - i, -1):
        sys.stdout.write(str(x))
    sys.stdout.write("\n")
