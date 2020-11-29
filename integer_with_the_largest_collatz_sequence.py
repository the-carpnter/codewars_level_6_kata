def collatz(n):
    return 1 + collatz(3*n+1 if n%2 else n//2) if n!=1 else 1

def longest_collatz(input_array):
    return max(input_array, key=collatz)
