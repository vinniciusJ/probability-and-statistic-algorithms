from utils import convertion

def calculate_variance(numbers):
    average = sum(numbers) / len(numbers)

    summation = sum([(n - average) ** 2 for n in numbers])
    variance = summation / (len(numbers) - 1)

    return variance


if __name__ == '__main__':
    numbers = [convertion.convert_to_number(x) for x in input('Informe a amostra: \n').split(' ')]

    variance = calculate_variance(numbers)

    print(f'A variança dessa amostra é {round(variance, 2)}')