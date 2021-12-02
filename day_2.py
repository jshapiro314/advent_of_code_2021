from typing import List, Tuple


def calculate_final_position(commands: List[Tuple[str, int]]) -> Tuple[int, int]:
    final_x = 0
    final_y = 0

    for direction, magnitude in commands:
        if direction == "forward":
            final_x += magnitude
        elif direction == "down":
            final_y += magnitude
        elif direction == "up":
            final_y -= magnitude

    return final_x, final_y


def calculate_final_position_with_aim(
    commands: List[Tuple[str, int]]
) -> Tuple[int, int]:
    final_x = 0
    final_y = 0
    aim = 0

    for direction, magnitude in commands:
        if direction == "forward":
            final_x += magnitude
            final_y += aim * magnitude
        elif direction == "down":
            aim += magnitude
        elif direction == "up":
            aim -= magnitude

    return final_x, final_y


if __name__ == "__main__":
    commands = []
    with open("day_2_input.txt") as f:
        for line in f:
            line = line.strip()
            direction, magnitude = line.split(" ")
            magnitude = int(magnitude)

            commands.append((direction, magnitude))

    final_x, final_y = calculate_final_position(commands)
    print(final_x * final_y)

    final_x, final_y = calculate_final_position_with_aim(commands)
    print(final_x * final_y)
