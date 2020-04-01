'''
Name: Badr Choubai
Professor: David Kramer
Class: CS 1030
Project: Python Project Three
'''
import sys


def print_search_results(results: tuple) -> None:
    '''print_search_results
    This method takes the results from the search_provinces method and pretty
    prints them.
    '''
    province_list, province_type = results
    for i, _ in enumerate(province_list):
        province_list[i] = province_list[i].replace('_', ' ').title()

    print(
        f'The Province Code you entered is for a {province_type} area \
            in {" or the ".join(province_list)}')


def is_valid_postal_code(postal_code_input: str) -> bool:
    '''is_valid_postal_code
    This method takes the postal code input and runs a series of checks
    to see whether or not it is a valid input.
    '''
    # if postal code starts with one of these letters it will be invalid
    invalid_letters = {'D', 'F', 'I', 'O', 'Q', 'U', 'W', 'Z'}
    valid_length = len(postal_code_input) == 7
    valid_format = postal_code_input[3].isspace()
    valid_letter = postal_code_input[0] not in invalid_letters

    return valid_length and valid_format and valid_letter


def search_provinces(postal_code_input: str) -> tuple:
    '''search_provinces
    This method takes the province code input and returns a tuple containing
    the province type and the province that matches the province code
    '''
    canadian_provinces = {
        'newfoundland': 'A',
        'nova_scotia': 'B',
        'prince_edward_island': 'C',
        'new_brunswick': 'E',
        'quebec': 'GHJ',
        'ontario': 'KLMNP',
        'manitoba': 'R',
        'saskatchewan': 'S',
        'alberta': 'T',
        'british_columbia': 'V',
        'nunavut': 'X',
        'northwest_territories': 'X',
        'yukon': 'Y',
    }
    province_type = 'Rural' if postal_code_input[1] == '0' else 'Urban'
    province_list = []

    letter = postal_code_input[0]
    for province, letters in canadian_provinces.items():
        if letter in letters:
            province_list.append(province)

    return (province_list, province_type)


def main():
    while True:
        postal_code_input = input("Enter a Canadian province code: ")

        if postal_code_input == '':
            sys.exit()
        elif is_valid_postal_code(postal_code_input):
            search_results = search_provinces(postal_code_input)
            print_search_results(search_results)
            continue
        else:
            print(
                f'Please enter a valid Canadian province code')


if __name__ == '__main__':
    main()
