# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.


sum=int(input("Петя сказал, что сумма чисел равна: "))
prod=int(input("Петя сказал, что произведение чисел равно: "))
for i in range(sum):
    for j in range(prod):
        if sum == i+j and prod == i*j:
            print("Петя задумал: ", i, j)