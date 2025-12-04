def parse_input(filepath: str) -> list[tuple[int, int]]:
    with open(filepath, "r", encoding="utf-8") as f:
        line = f.read().strip()
        ranges = []
        for range_str in line.split(","):
            range_str = range_str.strip()
            if not range_str:
                continue

            start, end = map(int, range_str.split("-"))
            ranges.append((start, end))

        return ranges


def find_invalid_ids(
    ranges: list[tuple[int, int]], *, strict_half: bool = False
) -> list[int]:
    invalid_ids = []

    for start, end in ranges:
        for num in range(start, end + 1):
            num_str = str(num)
            str_len = len(num_str)

            if strict_half:
                if str_len % 2 != 0:
                    continue

                half = str_len // 2
                if num_str[:half] == num_str[half:]:
                    invalid_ids.append(num)
            else:
                for segment_len in range(1, str_len // 2 + 1):
                    if str_len % segment_len != 0:
                        continue
                    segment = num_str[:segment_len]
                    repeat_count = str_len // segment_len

                    if repeat_count >= 2 and segment * repeat_count == num_str:
                        invalid_ids.append(num)
                        break

    return invalid_ids


if __name__ == "__main__":
    ranges = parse_input("input-2.txt")

    invalid_ids_part1 = find_invalid_ids(ranges, strict_half=True)
    print(f"Part 1 - Invalid IDs count: {len(invalid_ids_part1)}")
    print(f"Part 1 - Sum: {sum(invalid_ids_part1)}")

    invalid_ids_part2 = find_invalid_ids(ranges, strict_half=False)
    print(f"\nPart 2 - Invalid IDs count: {len(invalid_ids_part2)}")
    print(f"Part 2 - Sum: {sum(invalid_ids_part2)}")
