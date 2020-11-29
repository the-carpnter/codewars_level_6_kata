def collatz(n):
    def _collatz(n):
        if n!=1:
            if n%2:
                return [n] + _collatz(3*n+1)
            else:
                return [n] + _collatz(n//2)
        return [1]
    return '->'.join(map(str, _collatz(n)))
