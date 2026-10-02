def create_kuku_table():
    # 9行9列の九九表を2次元リストで返す
    # 全然わかんないところ
    table = []
    for row in range(1, 10):
        line = []
        for columns in range(1, 10):
            line.append(row * columns)
        table.append(line)

    return table


def main():
    table = create_kuku_table()
    for line in table:
        text = ""
        for number in line:
            text = text + str(number) + " "
        print(text)


if __name__ == "__main__":
    main()
