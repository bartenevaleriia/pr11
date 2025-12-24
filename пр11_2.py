solve = 0

for bulls in range(1,11):
    for cows in range(1,21):
        for calves in range(1,201):
            if bulls * 10 + cows * 5 + calves * 0.5 == 100:
                if bulls > 0 and cows > 0 and calves > 0:
                    sum = bulls + cows + calves
                    print('Быков:',bulls, 'Коров:',cows,'Телят:',calves, 'Всего:',sum, sep='\t')

                    solve += 1

print("Всего решений: ", solve)