def pow2(n: int) -> int:
    """Compute 2**n in O(log n) multiplications without using **, pow, or bit ops.
       Only valid for integer n >= 0 (returns an int)."""
    if n < 0:
        raise ValueError("n must be non-negative for this version")
    result = 1
    base = 2
    while n > 0:
        if n % 2 == 1:     # check lowest bit without bit ops
            result *= base
        base *= base
        n //= 2            # integer divide by 2 instead of shifting
    return result

# Examples
print(pow2(0))  # 1
print(pow2(10)) # 1024
    
    
for i in range(1,10):
    print(pow(i))
    
print(pow(100))
print(2**100)
    
    