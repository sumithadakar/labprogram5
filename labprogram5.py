import sys

if len(sys.argv) != 4:
    print("Usage: python simple_interest.py <principal> <rate> <time>")
    sys.exit()

principal = float(sys.argv[1])
rate = float(sys.argv[2])
time = float(sys.argv[3])

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)
