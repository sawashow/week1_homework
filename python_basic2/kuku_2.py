def create_kuku_table(rows, colmns):
    # rows行、columns列の掛け算表を2次元リストで返す
    lines = []
    for row in range(1, rows + 1):
        cells = []
        for column in range(1, colmns + 1):
            cells.append(row * column)
        lines.append(cells)
    return lines


def main():
    rows = int(input("行数を入力してください："))
    colmns = int(input("列数を入力してください："))
    lines = create_kuku_table(rows, colmns)
    for line in lines:
        for product in line:
            print(f"{product} ", end="")
        print()


if __name__ == "__main__":
    main()
