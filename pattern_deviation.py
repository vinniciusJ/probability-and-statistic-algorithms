from math import sqrt

from variance import calculate_variance
from utils import convertion

numbers = [convertion.convert_to_number(x) for x in input('Informe a amostra: \n').split(' ')]

result = sqrt(calculate_variance(numbers))

print(f'O desvio padrão da amostra é: {round(result, 2)}')