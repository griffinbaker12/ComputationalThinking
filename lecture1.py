from typing import Union

Primitives = Union[int, str, bool, float]


def fill(element: Primitives, row_n, col_n):
    return (
        element,
        row_n,
        col_n,
        [[element for _ in range(col_n)] for _ in range(row_n)],
    )


def mult_table(row_n, col_n):
    return [[col * row for col in range(1, col_n + 1)] for row in range(1, row_n + 1)]


def print_matrix(m, width=3):
    for row in m:
        r_to_print = ""
        for col in row:
            r_to_print += f"{col:<{width}}"
        print(r_to_print)


def main():
    element, row_n, col_n, filled = fill(1, 3, 4)
    print(f"{row_n}x{col_n} Array{{{type(element).__name__.capitalize()}}}")
    print_matrix(filled)

    print()
    print("Multiplication table")
    print_matrix(mult_table(5, 5), 5)


if __name__ == "__main__":
    main()
