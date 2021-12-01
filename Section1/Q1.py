def calc(n : int) -> int:
    if n <= 1:
        return 1
    else:
        return n * calc(n-1)

result = calc(10)
print(result)

result = calc(100)
print(result)