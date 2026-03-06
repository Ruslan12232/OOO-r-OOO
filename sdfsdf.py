n = int(input())

if 0 < n <= 20:
    if n == 0:
        f1 = 0
    else:
        f0, f1 = 0, 1
        for i in range(2, n + 1):
            f0, f1 = f1, f0 + f1
    print(f"f({n}) = {f1}")
else:
    print("Не пиши больше 10, ок?")
