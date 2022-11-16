def convert_to_number(string):
    try:
        return int(string)
    except:
        return float(string.replace(',', '.'))