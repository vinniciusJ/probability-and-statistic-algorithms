from prettytable import PrettyTable

from modules import percentile, convertion

percentile_bases = [ 25, 50, 75 ]

sample = [convertion.convert_to_number(x) for x in input('Informe a amostra: \n').split(' ')]
quartiles = [ percentile.calculate_percentile(x, sample) for x in percentile_bases  ]

table = PrettyTable(['Q1', 'Q2', 'Q3'])

table.add_row(quartiles)

print(table)
