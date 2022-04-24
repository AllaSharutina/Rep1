N = int(input('Введите приобретаемое количество билетов:\t'))
old = []
summ = 0
for number in range(N):
    old.append(int(input(f"Введите возраст посетителя {number + 1}\t")))
    if 18 <= old[number] <= 25:
        summ = summ + 990
    elif old[number] > 25:
        summ = summ + 1390
print("Сумма без скидки", summ)
if N > 3:
    summ = summ * 0.9
print("Сумма со скидкой (к оплате)", summ)
