from typing import List, Tuple


def parse_input(txt_file: str) -> List[Tuple[str, int]]:
    with open(txt_file, "r", encoding="utf-8") as f:
        return [(line[0], int(line[1:].strip())) for line in f if line.strip()]


def count_zero_hits(position: int, direction: str, steps: int) -> int:
    if steps <= 0:
        return 0

    k_first = (100 - position) if direction == "R" else position
    k_first = k_first or 100

    return 0 if k_first > steps else 1 + (steps - k_first) // 100


def apply_rotations(rotations: List[Tuple[str, int]], start: int) -> Tuple[int, int]:
    position = start
    final_zero_count = 0
    all_zero_count = 0

    for direction, steps in rotations:
        all_zero_count += count_zero_hits(position, direction, steps)

        position = (position + steps if direction == "R" else position - steps) % 100

        if position == 0:
            final_zero_count += 1

    return final_zero_count, all_zero_count


if __name__ == "__main__":
    rotations = parse_input("input-1.txt")
    start = 50
    part1, part2 = apply_rotations(rotations, start)
    
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
