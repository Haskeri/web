import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest


PROJECT_DIR = Path(__file__).resolve().parent
INTERPRETER = os.environ.get("INTERPRETER", sys.executable)


def run_script(filename, input_data=None, cwd=PROJECT_DIR):
    input_text = "\n".join(input_data) if input_data is not None else ""
    proc = subprocess.run(
        [INTERPRETER, filename],
        input=input_text,
        capture_output=True,
        text=True,
        check=False,
        cwd=cwd,
    )
    assert proc.returncode == 0, (
        f"Script {filename} failed with code {proc.returncode}.\n"
        f"stdout: {proc.stdout}\n"
        f"stderr: {proc.stderr}"
    )
    return proc.stdout.strip()


def copy_script(script_name, destination):
    shutil.copy(PROJECT_DIR / script_name, destination / script_name)


def test_hello_world():
    assert run_script("hello.py") == "Hello, World!"


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1", "Weird"),
        ("2", "Not Weird"),
        ("3", "Weird"),
        ("4", "Not Weird"),
        ("6", "Weird"),
        ("20", "Weird"),
        ("22", "Not Weird"),
        ("99", "Weird"),
    ],
)
def test_python_if_else(input_data, expected):
    assert run_script("python_if_else.py", [input_data]) == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (["1", "2"], ["3", "-1", "2"]),
        (["3", "5"], ["8", "-2", "15"]),
        (["10", "10"], ["20", "0", "100"]),
        (["10000000000", "1"], ["10000000001", "9999999999", "10000000000"]),
    ],
)
def test_arithmetic_operators(input_data, expected):
    assert run_script("arithmetic_operators.py", input_data).splitlines() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (["3", "5"], ["0", "0.6"]),
        (["10", "2"], ["5", "5.0"]),
        (["-7", "3"], ["-3", "-2.3333333333333335"]),
        (["5", "-2"], ["-3", "-2.5"]),
        (["10", "0"], ["Division by zero", "Division by zero"]),
    ],
)
def test_division(input_data, expected):
    assert run_script("division.py", input_data).splitlines() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1", ["0"]),
        ("3", ["0", "1", "4"]),
        ("5", ["0", "1", "4", "9", "16"]),
        ("0", []),
    ],
)
def test_loops(input_data, expected):
    output = run_script("loops.py", [input_data])
    assert output.splitlines() == expected if output else expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1", "1"),
        ("5", "12345"),
        ("10", "12345678910"),
        ("0", ""),
    ],
)
def test_print_function(input_data, expected):
    assert run_script("print_function.py", [input_data]) == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (["5", "2 3 6 6 5"], "5"),
        (["4", "1 2 3 4"], "3"),
        (["6", "10 10 10 9 8 9"], "9"),
        (["2", "7 7"], "7"),
    ],
)
def test_second_score(input_data, expected):
    assert run_script("second_score.py", input_data) == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            ["5", "Harry", "37.21", "Berry", "37.21", "Tina", "37.2", "Akriti", "41", "Harsh", "39"],
            ["Berry", "Harry"],
        ),
        (["4", "A", "1", "B", "2", "C", "3", "D", "4"], ["B"]),
        (["6", "z", "2.0", "a", "1.0", "m", "2.0", "b", "1.0", "c", "3.0", "d", "2.0"], ["d", "m", "z"]),
        (["3", "A", "1.0", "B", "1.0", "C", "1.0"], ["A", "B", "C"]),
    ],
)
def test_nested_list(input_data, expected):
    assert run_script("nested_list.py", input_data).splitlines() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            [
                "12",
                "insert 0 5",
                "insert 1 10",
                "insert 0 6",
                "print",
                "remove 6",
                "append 9",
                "append 1",
                "sort",
                "print",
                "pop",
                "reverse",
                "print",
            ],
            ["[6, 5, 10]", "[1, 5, 9, 10]", "[9, 5, 1]"],
        ),
        (
            ["9", "append 1", "append 2", "append 3", "remove 2", "print", "pop", "reverse", "print", "sort"],
            ["[1, 3]", "[1]"],
        ),
        (
            ["7", "insert 0 10", "insert 1 5", "insert 1 7", "sort", "print", "reverse", "print"],
            ["[5, 7, 10]", "[10, 7, 5]"],
        ),
        (["3", "print", "pop", "print"], ["[]", "[]"]),
    ],
)
def test_lists(input_data, expected):
    assert run_script("lists.py", input_data).splitlines() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Www.MosPolytech.ru", "wWW.mOSpOLYTECH.RU"),
        ("Pythonist 2", "pYTHONIST 2"),
        ("aBcD", "AbCd"),
        ("123_+=", "123_+="),
    ],
)
def test_swap_case(input_data, expected):
    assert run_script("swap_case.py", [input_data]) == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("this is a string", "this-is-a-string"),
        (" one   two  three ", "one-two-three"),
        ("single", "single"),
        ("", ""),
    ],
)
def test_split_and_join(input_data, expected):
    assert run_script("split_and_join.py", [input_data]) == expected


def test_max_word_default_file():
    assert run_script("max_word.py").splitlines() == ["сосредоточенности"]


def test_max_word_multiple_longest(tmp_path):
    copy_script("max_word.py", tmp_path)
    (tmp_path / "example.txt").write_text(
        "one, three! seven??\nAlpha beta_gamma",
        encoding="utf-8",
    )
    assert run_script("max_word.py", cwd=tmp_path).splitlines() == ["three", "seven", "Alpha", "gamma"]


def test_max_word_cyrillic(tmp_path):
    copy_script("max_word.py", tmp_path)
    (tmp_path / "example.txt").write_text(
        "Привет, мир! длинноеслово и ещё длинноеслово.",
        encoding="utf-8",
    )
    assert run_script("max_word.py", cwd=tmp_path).splitlines() == ["длинноеслово", "длинноеслово"]


def test_price_sum_default_file():
    assert run_script("price_sum.py") == "6842.84 5891.06 6810.90"


def test_price_sum_simple_csv(tmp_path):
    copy_script("price_sum.py", tmp_path)
    (tmp_path / "products.csv").write_text(
        "Продукт,Взрослый,Пенсионер,Ребенок\n"
        "x,1.10,2.20,3.30\n"
        "y,4.40,5.50,6.60\n",
        encoding="utf-8",
    )
    assert run_script("price_sum.py", cwd=tmp_path) == "5.50 7.70 9.90"


def test_price_sum_utf8_sig(tmp_path):
    copy_script("price_sum.py", tmp_path)
    (tmp_path / "products.csv").write_text(
        "Продукт,Взрослый,Пенсионер,Ребенок\n"
        "яблоко,0,1.01,2.02\n"
        "мясо,3.03,4.04,5.05\n",
        encoding="utf-8-sig",
    )
    assert run_script("price_sum.py", cwd=tmp_path) == "3.03 5.05 7.07"


@pytest.mark.parametrize(
    "first, second, expected",
    [
        ("abc", "cba", "YES"),
        ("ab", "abc", "NO"),
        ("a1!", "!1a", "YES"),
        ("Aa", "aA", "YES"),
        ("hello", "bello", "NO"),
    ],
)
def test_anagram(first, second, expected):
    assert run_script("anagram.py", [first, second]) == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (["3", "1 5", "2 3", "4 6", "3"], "2"),
        (["2", "0 10", "5 8", "5"], "2"),
        (["2", "0 10", "3 7", "10"], "1"),
        (["4", "1 2", "3 4", "5 6", "7 8", "11"], "0"),
    ],
)
def test_metro(input_data, expected):
    assert run_script("metro.py", input_data) == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("BANANA", "Stuart 12"),
        ("AEIOU", "Kevin 15"),
        ("BCDF", "Stuart 10"),
        ("ABC", "Draw"),
    ],
)
def test_minion_game(input_data, expected):
    assert run_script("minion_game.py", [input_data]) == expected


@pytest.mark.parametrize(
    "year, expected",
    [
        ("2000", "True"),
        ("1900", "False"),
        ("2016", "True"),
        ("2019", "False"),
        ("2400", "True"),
        ("2100", "False"),
    ],
)
def test_is_leap(year, expected):
    assert run_script("is_leap.py", [year]) == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (["3 2", "1 5 3", "3 1", "5 7"], "1"),
        (["5 2", "1 2 3 4 5", "6 7", "8 9"], "0"),
        (["6 2", "1 1 1 2 2 3", "1 3", "2 4"], "2"),
        (["4 1", "5 5 5 5", "1", "5"], "-4"),
    ],
)
def test_happiness(input_data, expected):
    assert run_script("happiness.py", input_data) == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            ["50 3", "gold 10 60", "silver 20 100", "copper 30 120"],
            ["silver 20.00 100.00", "copper 20.00 80.00", "gold 10.00 60.00"],
        ),
        (["5 2", "A 10 100", "B 4 20"], ["A 5.00 50.00"]),
        (["10 3", "map 0 30", "rum 5 25", "spice 10 60"], ["spice 10.00 60.00", "map 0.00 30.00"]),
        (["3 2", "gold coin 2 10", "silver bar 3 9"], ["gold coin 2.00 10.00", "silver bar 1.00 3.00"]),
    ],
)
def test_pirate_ship(input_data, expected):
    assert run_script("pirate_ship.py", input_data).splitlines() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (["2", "1 2", "3 4", "5 6", "7 8"], ["19 22", "43 50"]),
        (["3", "1 0 0", "0 1 0", "0 0 1", "2 3 4", "5 6 7", "8 9 10"], ["2 3 4", "5 6 7", "8 9 10"]),
        (["2", "-1 2", "3 0", "4 -2", "1 5"], ["-2 12", "12 -6"]),
        (["2", "0 0", "0 0", "1 2", "3 4"], ["0 0", "0 0"]),
    ],
)
def test_matrix_mult(input_data, expected):
    assert run_script("matrix_mult.py", input_data).splitlines() == expected
