import math

import pytest

from average_scores import compute_average_scores
from circle_square_mk import circle_square_mk
from complex_numbers import Complex
from email_validation import filter_mail, fun
from fact import fact_it, fact_rec
from fibonacci import cube, fibonacci
from file_search import find_file, read_first_lines, search_and_read
from files_sort import sort_files_by_extension
from log_decorator import function_logger
from my_sum import my_sum
from my_sum_argv import format_number, main as my_sum_argv_main, sum_from_argv
from people_sort import name_format
from phone_number import normalize_phone, sort_phone
from plane_angle import Point, plane_angle
from process_list import process_list, process_list_gen
from show_employee import show_employee
from sum_and_sub import sum_and_sub


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (5, 120),
        (10, 3628800),
        (20, 2432902008176640000),
    ],
)
def test_fact_it(n, expected):
    assert fact_it(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (5, 120),
        (10, 3628800),
        (20, 2432902008176640000),
    ],
)
def test_fact_rec(n, expected):
    assert fact_rec(n) == expected


def test_fact_large_equals_math_factorial():
    assert fact_it(50) == math.factorial(50)
    assert fact_rec(50) == math.factorial(50)


@pytest.mark.parametrize("func", [fact_it, fact_rec])
def test_fact_negative_raises(func):
    with pytest.raises(ValueError):
        func(-1)


@pytest.mark.parametrize("func", [fact_it, fact_rec])
def test_fact_non_int_raises(func):
    with pytest.raises(TypeError):
        func(2.5)


@pytest.mark.parametrize(
    "name, salary, expected",
    [
        ("Иванов Иван Иванович", 30000, "Иванов Иван Иванович: 30000 ₽"),
        ("Петров Петр", 0, "Петров Петр: 0 ₽"),
        ("Сидоров Сидор", 123456.78, "Сидоров Сидор: 123456.78 ₽"),
    ],
)
def test_show_employee(name, salary, expected):
    assert show_employee(name, salary) == expected


def test_show_employee_default_salary():
    assert show_employee("Тест") == "Тест: 100000 ₽"


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1.0, 2.0, (3.0, -1.0)),
        (10.5, 0.5, (11.0, 10.0)),
        (-2.0, -3.0, (-5.0, 1.0)),
        (0.0, 0.0, (0.0, 0.0)),
    ],
)
def test_sum_and_sub(a, b, expected):
    assert sum_and_sub(a, b) == expected


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3], [1, 4, 27]),
        ([0, -2, -3], [0, 4, -27]),
        ([10], [100]),
        ([-1], [-1]),
    ],
)
def test_process_list(arr, expected):
    assert process_list(arr) == expected


@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3], [1, 4, 27]),
        ([4, 5], [16, 125]),
        ([0], [0]),
    ],
)
def test_process_list_gen(arr, expected):
    assert list(process_list_gen(arr)) == expected


def test_process_list_and_gen_equal():
    source = list(range(-20, 21))
    assert process_list(source) == list(process_list_gen(source))


@pytest.mark.parametrize(
    "args, expected",
    [
        ((1, 2, 3), 6),
        ((1.5, 2.5), 4.0),
        ((), 0),
        ((-1, 1, -2, 2), 0),
    ],
)
def test_my_sum(args, expected):
    assert my_sum(*args) == expected


@pytest.mark.parametrize(
    "argv, expected",
    [
        (["1", "2", "3"], 6.0),
        (["1.5", "2", "3.5"], 7.0),
        (["-1", "1"], 0.0),
        (["0"], 0.0),
    ],
)
def test_sum_from_argv(argv, expected):
    assert sum_from_argv(argv) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        (15.0, "15"),
        (15.25, "15.25"),
        (-2.0, "-2"),
    ],
)
def test_format_number(value, expected):
    assert format_number(value) == expected


def test_my_sum_argv_main(capsys):
    result = my_sum_argv_main(["1", "2", "3", "4", "5"])
    captured = capsys.readouterr()
    assert result == 15.0
    assert captured.out.strip() == "15"


def test_sort_files_by_extension_grouping(tmp_path):
    (tmp_path / "a.py").write_text("", encoding="utf-8")
    (tmp_path / "a.txt").write_text("", encoding="utf-8")
    (tmp_path / "b.py").write_text("", encoding="utf-8")
    (tmp_path / "b.txt").write_text("", encoding="utf-8")
    (tmp_path / "c.py").write_text("", encoding="utf-8")
    (tmp_path / "c.txt").write_text("", encoding="utf-8")
    (tmp_path / "subdir").mkdir()

    assert sort_files_by_extension(tmp_path) == [
        "a.py",
        "b.py",
        "c.py",
        "a.txt",
        "b.txt",
        "c.txt",
    ]


def test_sort_files_by_extension_with_no_extension(tmp_path):
    (tmp_path / "readme").write_text("", encoding="utf-8")
    (tmp_path / "a.py").write_text("", encoding="utf-8")
    (tmp_path / "z.md").write_text("", encoding="utf-8")

    assert sort_files_by_extension(tmp_path) == ["readme", "a.py", "z.md"]


def test_sort_files_by_extension_empty_directory(tmp_path):
    assert sort_files_by_extension(tmp_path) == []


def test_find_file_found_in_nested_dir(tmp_path):
    nested = tmp_path / "a" / "b"
    nested.mkdir(parents=True)
    target = nested / "target.txt"
    target.write_text("line1\nline2\n", encoding="utf-8")

    found = find_file("target.txt", start_dir=tmp_path)
    assert found is not None
    assert found.name == "target.txt"
    assert found == target


def test_find_file_not_found(tmp_path):
    (tmp_path / "data.txt").write_text("x", encoding="utf-8")
    assert find_file("missing.txt", start_dir=tmp_path) is None


def test_read_first_lines_less_than_five(tmp_path):
    file_path = tmp_path / "data.txt"
    file_path.write_text("a\nb\nc\n", encoding="utf-8")
    assert read_first_lines(file_path, 5) == ["a", "b", "c"]


def test_read_first_lines_exact_five(tmp_path):
    file_path = tmp_path / "data.txt"
    file_path.write_text("1\n2\n3\n4\n5\n6\n", encoding="utf-8")
    assert read_first_lines(file_path, 5) == ["1", "2", "3", "4", "5"]


def test_search_and_read_found(tmp_path):
    nested = tmp_path / "x" / "y"
    nested.mkdir(parents=True)
    (nested / "book.txt").write_text("l1\nl2\nl3\nl4\nl5\nl6\n", encoding="utf-8")

    assert search_and_read("book.txt", start_dir=tmp_path) == "l1\nl2\nl3\nl4\nl5"


def test_search_and_read_not_found(tmp_path):
    assert search_and_read("ghost.txt", start_dir=tmp_path) == "Файл ghost.txt не найден"


@pytest.mark.parametrize(
    "address, expected",
    [
        ("lara@mospolytech.ru", True),
        ("brian-23@mospolytech.ru", True),
        ("britts_54@mospolytech.ru", True),
        ("A1_b-c@abc.io", True),
        ("a@b.c", True),
        ("with.dot@site.ru", False),
        ("name@site.comm", False),
        ("name@site.c0", False),
        ("name@site", False),
        ("name@si-te.ru", False),
        ("name@@site.ru", False),
        ("name site@site.ru", False),
    ],
)
def test_email_fun(address, expected):
    assert fun(address) is expected


def test_filter_mail_and_sort():
    emails = [
        "bad.mail@site.ru",
        "z_user@abc.ru",
        "alpha@site.com",
        "name@site.comm",
        "beta-1@abc.ru",
    ]
    result = sorted(filter_mail(emails))
    assert result == ["beta-1@abc.ru", "z_user@abc.ru"]


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, []),
        (1, [0]),
        (2, [0, 1]),
        (5, [0, 1, 1, 2, 3]),
        (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
    ],
)
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected


@pytest.mark.parametrize(
    "n, expected",
    [
        (5, [0, 1, 1, 8, 27]),
        (7, [0, 1, 1, 8, 27, 125, 512]),
    ],
)
def test_fibonacci_cubes(n, expected):
    assert list(map(cube, fibonacci(n))) == expected


@pytest.mark.parametrize(
    "scores, expected",
    [
        (
            [
                (89, 90, 78, 93, 80),
                (90, 91, 85, 88, 86),
                (91, 92, 83, 89, 90.5),
            ],
            (90.0, 91.0, 82.0, 90.0, 85.5),
        ),
        ([(100, 0), (0, 100)], (50.0, 50.0)),
        ([(10, 20, 30)], (10.0, 20.0, 30.0)),
        ([], tuple()),
    ],
)
def test_compute_average_scores(scores, expected):
    assert compute_average_scores(scores) == expected


def test_plane_angle_zero_degrees():
    a = Point(0, 0, 0)
    b = Point(1, 0, 0)
    c = Point(1, 1, 0)
    d = Point(2, 1, 0)
    assert plane_angle(a, b, c, d) == pytest.approx(0.0, abs=1e-6)


def test_plane_angle_ninety_degrees():
    a = Point(0, 0, 0)
    b = Point(1, 0, 0)
    c = Point(1, 1, 0)
    d = Point(1, 1, 1)
    assert plane_angle(a, b, c, d) == pytest.approx(90.0, abs=1e-6)


def test_plane_angle_degenerate_returns_zero():
    a = Point(0, 0, 0)
    b = Point(1, 1, 1)
    c = Point(2, 2, 2)
    d = Point(3, 3, 3)
    assert plane_angle(a, b, c, d) == 0.0


@pytest.mark.parametrize(
    "raw, expected",
    [
        ("07895462130", "+7 (789) 546-21-30"),
        ("89875641230", "+7 (987) 564-12-30"),
        ("9195969878", "+7 (919) 596-98-78"),
        ("+7 919 596 98 78", "+7 (919) 596-98-78"),
        ("007895462130", "+7 (789) 546-21-30"),
    ],
)
def test_normalize_phone(raw, expected):
    assert normalize_phone(raw) == expected


def test_normalize_phone_invalid():
    with pytest.raises(ValueError):
        normalize_phone("123")


def test_sort_phone_sample():
    raw = ["07895462130", "89875641230", "9195969878"]
    assert sort_phone(raw) == [
        "+7 (789) 546-21-30",
        "+7 (919) 596-98-78",
        "+7 (987) 564-12-30",
    ]


def test_sort_phone_with_equal_prefixes():
    raw = ["89100000000", "89100000001", "89100000002"]
    assert sort_phone(raw) == [
        "+7 (910) 000-00-00",
        "+7 (910) 000-00-01",
        "+7 (910) 000-00-02",
    ]


def test_people_sort_basic():
    people = [
        ["Mike", "Thomson", "20", "M"],
        ["Robert", "Bustle", "32", "M"],
        ["Andria", "Bustle", "30", "F"],
    ]
    assert name_format(people) == [
        "Mr. Mike Thomson",
        "Ms. Andria Bustle",
        "Mr. Robert Bustle",
    ]


def test_people_sort_stable_for_equal_ages():
    people = [
        ["A", "One", "25", "M"],
        ["B", "Two", "25", "F"],
        ["C", "Three", "24", "M"],
    ]
    assert name_format(people) == [
        "Mr. C Three",
        "Mr. A One",
        "Ms. B Two",
    ]


def test_complex_add():
    c = Complex(2, 1)
    d = Complex(5, 6)
    assert str(c + d) == "7.00+7.00i"


def test_complex_sub():
    c = Complex(2, 1)
    d = Complex(5, 6)
    assert str(c - d) == "-3.00-5.00i"


def test_complex_mul():
    c = Complex(2, 1)
    d = Complex(5, 6)
    assert str(c * d) == "4.00+17.00i"


def test_complex_div():
    c = Complex(2, 1)
    d = Complex(5, 6)
    assert str(c / d) == "0.26-0.11i"


def test_complex_mod_values():
    c = Complex(2, 1)
    d = Complex(5, 6)
    assert str(c.mod()) == "2.24+0.00i"
    assert str(d.mod()) == "7.81+0.00i"


def test_complex_zero_division():
    c = Complex(1, 1)
    with pytest.raises(ZeroDivisionError):
        _ = c / Complex(0, 0)


@pytest.mark.parametrize(
    "real, imag, expected",
    [
        (3, 0, "3.00+0.00i"),
        (0, 3, "0.00+3.00i"),
        (0, -3, "0.00-3.00i"),
    ],
)
def test_complex_format_variants(real, imag, expected):
    assert str(Complex(real, imag)) == expected


def test_circle_square_mk_close_to_formula_small_n():
    approx_value = circle_square_mk(1, 1000)
    assert abs(approx_value - math.pi) < 0.3


def test_circle_square_mk_close_to_formula_large_n():
    approx_value = circle_square_mk(3, 10000)
    assert abs(approx_value - math.pi * 9) < 0.6


def test_circle_square_mk_invalid_n():
    with pytest.raises(ValueError):
        circle_square_mk(2, 0)


def test_function_logger_creates_file_and_logs_values(tmp_path):
    log_path = tmp_path / "test.log"

    @function_logger(log_path)
    def greeting_format(name):
        return f"Hello, {name}!"

    assert greeting_format("John") == "Hello, John!"

    content = log_path.read_text(encoding="utf-8").splitlines()
    assert content[0] == "greeting_format"
    assert content[2] == "('John',)"
    assert content[4] == "Hello, John!"
    assert float(content[6]) >= 0.0


def test_function_logger_logs_none_as_dash(tmp_path):
    log_path = tmp_path / "test.log"

    @function_logger(log_path)
    def no_return():
        return None

    no_return()
    content = log_path.read_text(encoding="utf-8").splitlines()
    assert content[4] == "-"


def test_function_logger_appends_logs(tmp_path):
    log_path = tmp_path / "test.log"

    @function_logger(log_path)
    def add(a, b):
        return a + b

    add(1, 2)
    add(3, 4)

    content = log_path.read_text(encoding="utf-8").splitlines()
    # На один вызов приходится 7 строк, значит после двух вызовов их 14.
    assert len(content) == 14
    assert content[0] == "add"
    assert content[7] == "add"
