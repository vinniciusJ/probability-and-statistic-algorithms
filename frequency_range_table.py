from math import ceil, sqrt
from prettytable import PrettyTable

def string_to_number(string):
    try:
        return int(string)
    except:
        return float(string.replace(',', '.'))

numbers = [string_to_number(x) for x in input('Informe a amostra: \n').split(' ')]

k = ceil(sqrt(len(numbers)))
total_range = max(numbers) - min(numbers)
sample_range = total_range / k

categories = [min(numbers) + (sample_range * (x + 1)) for x in range(k)]

table = PrettyTable(['Categoria', 'Intervalo', 'fi', 'Fi', 'fr_i', 'Fr_i'])
filtered_by_category = []

for index, category in enumerate(categories):
    filtered = []
    period = ''

    for number in numbers: 
        if index == 0:
            if min(numbers) <= number <= category:
                filtered.append(number)
                period =  f'[{min(numbers)}, {category})'
                
        elif index + 1 == len(categories):
            if category <= number <= max(numbers):
                filtered.append(number)
                period =  f'[{category}, {max(numbers)}]'
        else:
            if categories[index - 1] <= number and number < category:
                filtered.append(number)
                period = f'[{categories[index - 1]}, {category})'

    fi = len(filtered)
    fr_i = fi / len(numbers)
    Fi = fi + sum(len(previous) for previous in filtered_by_category)
    Fr_i = fr_i + sum((len(previous) / len(numbers)) for previous in filtered_by_category)

    filtered_by_category.append(filtered)
    
    table.add_row([(index + 1), period, fi,  Fi,  fr_i,  Fr_i ])

print(table)