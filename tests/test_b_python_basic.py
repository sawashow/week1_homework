import sys
from pathlib import Path

# tests/ フォルダーから python_basic2/ フォルダーのファイルを読み込むための準備
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))


def test_b_1():
    from python_basic2.kuku_1 import create_kuku_table

    table = create_kuku_table()

    assert table[0] == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert table[8] == [9, 18, 27, 36, 45, 54, 63, 72, 81]
    print("B-1 OK")


def test_b_2():
    from python_basic2.kuku_2 import create_kuku_table

    assert create_kuku_table(4, 6) == [
        [1, 2, 3, 4, 5, 6],
        [2, 4, 6, 8, 10, 12],
        [3, 6, 9, 12, 15, 18],
        [4, 8, 12, 16, 20, 24],
    ]
    print("B-2 OK")


def main():
    test_b_1()
    test_b_2()


if __name__ == "__main__":
    main()
