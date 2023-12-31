# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии


names = ["Вера", "Надежда", "Любовь"]
rates = [1000, 1500, 1200]
bonuses = ["10.25%", "8.75%", "12.21%"]

result_dict = {name: rate * float(bonus[:-1]) / 100 for name, rate, bonus in zip(names, rates, bonuses)}

print(result_dict)