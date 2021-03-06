KILO_TO_POUND = 2.204623
POUND_TO_KILO = 0.453592


def main():
    value = input('Please select your measuring value in Kilos (K) or Pounds (P): ').lower()
    valid_weight = False
    while not valid_weight:
        weight = input('Please enter the weight to convert (numbers only): ')
        try:
            weight = float(weight)
            valid_weight = True
            break
        except ValueError:
            print(ValueError('Weight must be a number'))
            continue

    if value == 'p':
        result = convert_pounds_to_kilos(weight)
        print(f'The weight of {weight} pounds is equal to {round(result, 2)} kilos.')
    elif value == 'k':
        result = convert_kilos_to_pounds(weight)
        print(f'The weight of {weight} kilos is equal to {round(result, 2)} pounds.')
    else:
        print('Could not find the conversion value you entered, closing program.')


def convert_pounds_to_kilos(weight):
    return weight * POUND_TO_KILO


def convert_kilos_to_pounds(weight):
    return weight * KILO_TO_POUND


if __name__ == "__main__":
    main()
