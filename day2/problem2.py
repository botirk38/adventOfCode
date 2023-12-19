max_cube_count = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def is_game_possible(game_data):
    draws = game_data.split(":")[1].split(";")
    
    for draw in draws:
        for cube in draw.split(","):
            num, color = cube.split()
            print(num, color)
            if int(num) > max_cube_count[color]:
                return False
    return True

def minimum_set_cubes(game_data):
    draws = game_data.split(":")[1].split(";")
    total_power = 0
    red_cube, green_cube, blue_cube = 1, 1, 1
    for draw in draws:

        for cube in draw.split(","):
            num, color = cube.split()

            if color == "red":
                red_cube = max(red_cube, int(num))
            elif color == "green":
                green_cube = max(green_cube, int(num))
            elif color == "blue":
                blue_cube = max(blue_cube, int(num))

    return red_cube * green_cube * blue_cube

def process_file(file_path):
    possible_games_sum = 0
    with open(file_path, 'r') as file:
        for index, line in enumerate(file):
            if is_game_possible(line):
                possible_games_sum += index + 1
    return possible_games_sum

def process_file_2(file_path):
    minimum_set_cubes_sum = 0
    with open(file_path, 'r') as f:
        for line in f:
            minimum_set_cubes_sum += minimum_set_cubes(line)
    return minimum_set_cubes_sum


file_path = 'test.txt'  
result = process_file_2(file_path)
print(result)
