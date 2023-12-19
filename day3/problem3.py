DIRECTIONS = [
    (-1, -1), # Top-left
    (-1, 0),  # Up
    (-1, 1),  # Top-right
    (0, -1),  # Left
    (0, 1),   # Right
    (1, -1),  # Bottom-left
    (1, 0),   # Down
    (1, 1)    # Bottom-right
]

def is_valid_symbol(char):
    return not (char.isdigit() or char == '.')

def is_adjacent_to_symbol(schematic, processed_locations, row, col):
    for dx, dy in DIRECTIONS:
        if 0 <= row + dx < len(schematic) and 0 <= col + dy < len(schematic[row + dx]):
            if is_valid_symbol(schematic[row + dx][col + dy]):
                return True
    return False

def calculate_sum_of_part_numbers(schematic):
    schematic = [list(line) for line in schematic.split('\n')]
    processed_locations = set()
    total_sum = 0

    for i, row in enumerate(schematic):
        j = 0
        while j < len(row):
            if row[j].isdigit() and (i, j) not in processed_locations:
                number, init_j = row[j], j
                while j + 1 < len(row) and row[j + 1].isdigit():
                    number += row[j + 1]
                    j += 1
                
                for col_index in range(init_j, j + 1):
                    processed_locations.add((i, col_index))
                    if is_adjacent_to_symbol(schematic, processed_locations, i, col_index):
                        total_sum += int(number)
                        break
            j += 1
        
    return total_sum


def get_full_part_number(schematic, row, col):
    number_str = schematic[row][col]
    left_col = col - 1
    while left_col >= 0 and schematic[row][left_col].isdigit():
        number_str = schematic[row][left_col] + number_str
        left_col -= 1
    right_col = col + 1
    while right_col < len(schematic[row]) and schematic[row][right_col].isdigit():
        number_str += schematic[row][right_col]
        right_col += 1
    return int(number_str)

def calculate_sum_gear_ratios(schematic):
    schematic = [list(line) for line in schematic.split('\n')]
    gear_ratio_sum = 0

    for i, row in enumerate(schematic):
        for j, cell in enumerate(row):
            if cell == '*':
                adjacent_numbers = []
                for dx, dy in DIRECTIONS:
                    adjacent_row, adjacent_col = i + dx, j + dy
                    if 0 <= adjacent_row < len(schematic) and 0 <= adjacent_col < len(schematic[adjacent_row]) and schematic[adjacent_row][adjacent_col].isdigit():
                        part_number = get_full_part_number(schematic, adjacent_row, adjacent_col)
                        if part_number not in adjacent_numbers:
                            adjacent_numbers.append(part_number)
                if len(adjacent_numbers) == 2:
                    gear_ratio_sum += adjacent_numbers[0] * adjacent_numbers[1]
    return gear_ratio_sum






def main():
    with open("test.txt") as file:
        engine_schematic = file.read()

    total_sum = calculate_sum_of_part_numbers(engine_schematic)
    print(f"Sum of part numbers is {total_sum}")
    gear_ratio = calculate_sum_gear_ratios(engine_schematic)
    print(f"Sum of gear ratios is {gear_ratio}")




if __name__ == "__main__":
    # test_sum_of_part_numbers()
    main()
