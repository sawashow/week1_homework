def format_kuku(rows, columns):
    # 各行の文字列をリストで返す
    lines = []
    for row in range(1, rows + 1):
        cells = []
        for column in range(1, columns + 1):
            product = row * column
            if product < 10:
                expression = f"{column} x {row} =  {column*row}"
            else:
                expression = f"{column} x {row} = {column*row}"
            cells.append(f"{expression} | ")
        lines.append("".join(cells))

    return lines
