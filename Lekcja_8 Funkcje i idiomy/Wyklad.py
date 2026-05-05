wagi = [70, 85, 62, 95, 78]
wzrosty = [1.75, 1.80, 1.65, 1.78, 1.72]

for i in range(len(wagi)):
    BMI = wagi[i]/wzrosty[i]**2
    if BMI < 18.5:
        kat = 'niedowaga'
    elif BMI < 25:
        kat = 'norma'
    else:
        kat = 'nadwaga'
    print(f"waga: {wagi[i]}, wzrost: {wzrosty[i]:.2f}, BMI  {BMI:.2f}, {kat:<9}")