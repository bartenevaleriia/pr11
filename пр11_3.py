def find_solution():
    for a in range(1, 151):
        a5 = a ** 5

        for b in range(a, 151):
            b5 = b ** 5

            for c in range(b, 151):
                c5 = c ** 5

                for d in range(c, 151):
                    total = a5 + b5 + c5 + d ** 5
                    e = int(total ** (1 / 5))

                    if e ** 5 == total and e <= 150:
                        return a + b + c + d + e
    return None


result = find_solution()
if result is not None:
    print(f'Сумма всех чисел, удовлетворяющих условию: {result}')