
def convert_seed(seed, mappings):
    for dest_start, src_start, range_len in mappings:
        if src_start <= seed < src_start + range_len:
            seed = dest_start + (seed - src_start)
            break
    return seed


def read_seeds(seed_line):
    seed_ranges = list(map(int, seed_line.split()[1:]))
    sorted_ranges = sorted([(seed_ranges[i], seed_ranges[i + 1]) for i in range(0, len(seed_ranges), 2)], key=lambda x: x[0])

    merged_ranges = []
    current_start, current_length = sorted_ranges[0]

    for i in range(1, len(sorted_ranges)):
        start, length = sorted_ranges[i]
        if start <= current_start + current_length:  # Overlap detected
            # Extend the current range to include the new range
            current_length = max(current_start + current_length, start + length) - current_start
        else:
            # No overlap, add the current range to merged ranges and start a new range
            merged_ranges.append((current_start, current_length))
            current_start, current_length = start, length

    # Add the last range
    merged_ranges.append((current_start, current_length))

    # Convert ranges to list of seeds
    seeds = []
    for start, length in merged_ranges:
        seeds.extend(range(start, start + length))

    return seeds




def read_mappings(file):
    mappings = []
    mapping = []

    # Read mappings
    for line in file:
        # Check if the line is part of a mapping
        if len(line.split()) == 3:
            mapping.append(tuple(map(int, line.split())))
        else:
            # Add the last mapping if not empty
            if mapping:
                mappings.append(mapping)
            mapping = []

    # Add the last mapping if not empty
    if mapping:
        mappings.append(mapping)

    return mappings


def parse_file(filename):
    with open(filename, "r") as file:
        # Read seeds
        seeds_line = file.readline().strip()
        seeds = list(map(int, seeds_line.split()[1:]))
        print("Seeds:", seeds)

        mappings = []
        mapping = []

        # Read mappings
        for line in file:
            # Check if the line is part of a mapping
            if len(line.split()) == 3:
                mapping.append(tuple(map(int, line.split())))
            else:
                # Add the last mapping if not empty
                if mapping:
                    mappings.append(mapping)
                mapping = []
        if mapping:
            mappings.append(mapping)
        print("Mappings:", mappings)

        # Apply mappings to seeds
        locations = []
        for seed in seeds:
            res = seed
            for mapping in mappings:
                res = convert_seed(res, mapping)
            locations.append(res)

        return min(locations)




def parse_file_2(filename):
    with open(filename, "r") as file:
        # Read seeds
        seeds_line = file.readline().strip()
        seeds = read_seeds(seeds_line)
        print("Seeds:", seeds)

        mappings = []
        mapping = []

        # Read mappings
        for line in file:
            # Check if the line is part of a mapping
            if len(line.split()) == 3:
                mapping.append(tuple(map(int, line.split())))
            else:
                # Add the last mapping if not empty
                if mapping:
                    mappings.append(mapping)
                mapping = []
        if mapping:
            mappings.append(mapping)
        print("Mappings:", mappings)

        # Apply mappings to seeds
        locations = []
        for seed in seeds:
            res = seed
            for mapping in mappings:
                res = convert_seed(res, mapping)
            locations.append(res)

        return min(locations)




if __name__ == "__main__":

    print(parse_file("test.txt"))
    print(parse_file_2("test.txt"))
