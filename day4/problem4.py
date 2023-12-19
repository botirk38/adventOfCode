
def calculate_points(file_name: str) -> int:
    total_points = 0

    with open(file_name, "r") as file:
        for line in file:
            # Split the line to remove the "Card n:" part
            _, numbers = line.strip().split(": ")
            winning_numbers_str, my_numbers_str = numbers.split(" | ")
            winning_numbers = set(map(int, winning_numbers_str.split()))
            my_numbers = map(int, my_numbers_str.split())

            points = 0
            for num in my_numbers:
                if num in winning_numbers:
                    points = 1 if points == 0 else points * 2

            total_points += points

    return total_points



def calculate_total_scratchcards(file_name: str) -> int:
    def count_matches(card, winning_numbers):
        return sum(1 for num in card if num in winning_numbers)

    def process_card(index, matches, card_count, scratch_cards):
        new_count = card_count
        for i in range(1, matches + 1):
            if index + i < len(scratch_cards):
                winning_numbers, my_numbers = scratch_cards[index + i]
                next_matches = count_matches(my_numbers, winning_numbers)
                new_count += 1
                new_count = process_card(index + i, next_matches, new_count, scratch_cards)
        return new_count

    scratch_cards = []

    with open(file_name, "r") as file:
        for line in file:
            _, numbers = line.strip().split(": ")
            winning_numbers_str, my_numbers_str = numbers.split(" | ")
            winning_numbers = set(map(int, winning_numbers_str.split()))
            my_numbers = list(map(int, my_numbers_str.split()))
            scratch_cards.append((winning_numbers, my_numbers))

    total_count = 0
    for i in range(len(scratch_cards)):
        winning_numbers, my_numbers = scratch_cards[i]
        matches = count_matches(my_numbers, winning_numbers)
        total_count += 1  # Count the card itself
        total_count = process_card(i, matches, total_count, scratch_cards)  # Count copies

    return total_count


if  __name__ == "__main__":
    res = calculate_points("sample.txt")
    print(res)
    res2 = calculate_total_scratchcards("sample.txt")
    print(res2)

