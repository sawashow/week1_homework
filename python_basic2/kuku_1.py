def create_kuku_table():
    # 9行9列の九九表を2次元リストで返す
    lines = []
    for row in range(1, 10):
        cells = []
        for columns in range(1, 10):
            cells.append(row * columns)
        lines.append(cells)

    return lines


def main():
    lines = create_kuku_table()
    for cells in lines:
        text = ""
        for number in cells:
            text = text + str(number) + " "
        print(text)


if __name__ == "__main__":
    main()
