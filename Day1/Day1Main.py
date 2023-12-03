import regex as re

def parse_day_1_input_part_1(filename):
    calibrationSum = 0
    with open(filename, 'r') as file:
        for line in file:
            num1Str = next(char for char in line if char.isdigit())
            num2Str = next(char for char in reversed(line) if char.isdigit())
            calibrationSum += int(num1Str + num2Str)
    return calibrationSum

def string_to_int_string(string):
    match string:
        case 'one':
            return '1'
        case 'two':
            return '2'
        case 'three':
            return '3'
        case 'four':
            return '4'
        case 'five':
            return '5'
        case 'six':
            return '6'
        case 'seven':
            return '7'
        case 'eight':
            return '8'
        case 'nine':
            return '9'
        case _:
            return string

def parse_day_1_input_part_2(filename):
    calibrationSum = 0
    with open(filename, 'r') as file:
        for line in file:
            matches = re.findall(r'(one|two|three|four|five|six|seven|eight|nine|\d)', line, overlapped=True)
            num1Str = string_to_int_string(matches[0])
            num2Str = string_to_int_string(matches[-1])
            calibrationSum += int(num1Str + num2Str)
    return calibrationSum


if __name__ == '__main__':
    print(parse_day_1_input_part_1('Day1Input.txt'))
    print(parse_day_1_input_part_2('Day1Input.txt'))