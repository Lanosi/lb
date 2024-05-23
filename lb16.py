firms = {
    "Apple": "Воронеж",
    "Google": "Иваново",
    "Microsoft": "Нижнекамск",
    "Рога и копыта": "Париж",
    "Netflix": "Кугеси"
}

#2
keys = list(firms.keys())
print("Список ключей:", keys)

print("\nПары ключ-значение:")
for key, value in firms.items():
    print(f"{key} - {value}")

firm_name = input("Введите название компании: ")
if firm_name in firms:
    city = firms[firm_name]
    print(f"Фирма {firm_name} находится в {city}.")
else:
    print(f"Информация о фирме {firm_name} отсутствует.")

#3
new_dict_f = {}
for firm, city in firms.items():
    if city in new_dict_f:
        new_dict_f[city].append(firm)
    else:
        new_dict_f[city] = [firm]

print(new_dict_f)
