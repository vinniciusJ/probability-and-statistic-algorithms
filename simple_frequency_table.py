from prettytable import PrettyTable

numbers = [x for x in input('Informe a amostra: \n').split(' ')]
categories = set(numbers)

table = PrettyTable(['Categoria', 'fi', 'Fi', 'fr_i', 'Fr_i'])
filtered_by_category = []

for category in categories:
    filtered = list(filter(lambda number: number == category, numbers))

    fi = len(filtered)
    fr_i = fi / len(numbers)
    Fi = fi + sum(len(previous) for previous in filtered_by_category)
    Fr_i = fr_i + sum((len(previous) / len(numbers)) for previous in filtered_by_category)

    filtered_by_category.append(filtered)
    
    table.add_row([category, fi, Fi, fr_i, Fr_i])

print(table)