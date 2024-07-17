def fill(element, row_n, col_n):
    return (
        element,
        row_n,
        col_n,
        [[element for _ in range(col_n)] for _ in range(row_n)],
    )


def main():
    element, row_n, col_n, filled = fill(1, 3, 4)
    print(f"{row_n}x{col_n} Array{{{type(element).__name__.capitalize()}}}")
    for row in filled:
        r_to_print = ""
        for col in row:
            r_to_print += f"{col:<3}"
        print(r_to_print)


if __name__ == "__main__":
    main()
