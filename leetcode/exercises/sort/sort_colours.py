"""
# Statement

Given an array, colors, which contains a combination of the following three elements:
0 (Representing red)
1 (Representing white)
2 (Representing blue)

Sort the array in place so that the elements of the same color are adjacent, and the final order is: red (0), then white
(1), and then blue (2).

Note: You are not allowed to use any built-in sorting functions. The goal is to solve this efficiently without extra space.
"""
def sort_colours(colours):
    reds = 0
    whites = 0
    blues = 0
    for colour in colours:
        if colour == 0:
            reds += 1
        elif colour == 1:
            whites += 1
        elif colour == 2:
            blues += 1

    return [0 for _ in range(reds)] + [1 for _ in range(whites)] + [2 for _ in range(blues)]


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(
        description="Sort colour arrays (0, 1, 2) for quick debugging",
    )
    parser.add_argument(
        "cases",
        nargs="*",
        default=[
            "2,0,1",
        ],
        help="Space- or comma-delimited arrays of digits",
    )
    args = parser.parse_args()

    def parse_case(raw: str):
        tokens = [token for token in raw.replace(",", " ").split() if token]
        return [int(token) for token in tokens]

    for raw in args.cases:
        numbers = parse_case(raw)
        sorted_numbers = sort_colours(numbers[:])
        print(f"{numbers} -> {sorted_numbers}")


if __name__ == "__main__":
    main()
