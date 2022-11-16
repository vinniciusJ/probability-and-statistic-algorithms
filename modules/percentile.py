from math import ceil

from convertion import convert_to_number

def calculate_percentile(base, numbers):
    numbers.sort()

    index = (base / 100) * len(numbers)
    index = int(index) if int(index) == index else ceil(index) # O resultado pode ser 1.0 q é um "inteiro"

    if(isinstance(index, float)):
        return numbers[index - 1]

    if(isinstance(index, int)):
        reference_numbers = numbers[index - 1:index + 1]

        return sum(reference_numbers) / len(reference_numbers)

    return 0

def main():
    percentile_base = int(input('Informe a base: '))
    sample = [convert_to_number(x) for x in input('Informe a amostra: ').split(' ')]

    result = calculate_percentile(percentile_base, sample)

    print(f'O percentil de {percentile_base} é {result}')

if __name__ == '__main__':
    main()