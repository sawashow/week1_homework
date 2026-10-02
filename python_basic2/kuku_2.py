def create_kuku_table(rows, colmns):
    # rows行、columns列の掛け算表を2次元リストで返す
    table = []
    for row in range(1, rows + 1):
        line = []
        for column in range(1, 1 + colmns):
            line.append(row * column)
        table.append(line)
    return table


def main():
    rows = int(input("行数を入力してください："))
    colmns = int(input("列数を入力してください："))
    table = create_kuku_table(rows, colmns)
    for line in table:
        text = ""
        for number in line:
            text = text + str(number) + " "
        print(text)


if __name__ == "__main__":
    main()
