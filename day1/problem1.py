from typing import List, Optional


def find_sum_line(file: str) -> int:
  
    total = 0
    with open(file) as f:
        for line in f:
            first_digit = last_digit = None
            for char in line:
                if char.isdigit():
                    if first_digit is None:
                        first_digit = char
                    last_digit = char
            if first_digit and last_digit:
                total += int(first_digit + last_digit)

    return total

def read_prefix_numeral(chars: List[str]) -> Optional[int]:
    match chars:
        case ['o', 'n', 'e', *_]: return 1
        case ['t', 'w', 'o', *_]: return 2
        case ['t', 'h', 'r', 'e', 'e', *_]: return 3
        case ['f', 'o', 'u', 'r', *_]: return 4
        case ['f', 'i', 'v', 'e', *_]: return 5
        case ['s', 'i', 'x', *_]: return 6
        case ['s', 'e', 'v', 'e', 'n', *_]: return 7
        case ['e', 'i', 'g', 'h', 't', *_]: return 8
        case ['n', 'i', 'n', 'e', *_]: return 9
        case _: return None


# "two" or 2
def get_all_numerals(chars: List[str]) -> list[int]:
    match chars:
        case [c, *cs] if c.isnumeric():
            return [int(c), *get_all_numerals(cs)]
        case [_, *cs]:
            maybe_numeral = read_prefix_numeral(chars)
            if maybe_numeral is not None:
                return [maybe_numeral, *get_all_numerals(cs)]
            else:
                return get_all_numerals(cs)
        case _:
            return []


def get_value_(ints: List[int]) -> int:
    first = ints[0]
    last = ints[-1]
    return first * 10 + last


def main():
    handle = open('resources/input4.txt', 'r')
    text = handle.read()
    handle.close()

    lines = text.splitlines()
    numerals = map(lambda l: get_all_numerals(list(l)), lines)
    values = map(get_value_, numerals)
    print(sum(values))


if __name__ == '__main__':
    main()





