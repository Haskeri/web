import sys

from my_sum import my_sum


def sum_from_argv(args):
    return my_sum(*(float(value) for value in args))


def format_number(value):
    return str(int(value)) if float(value).is_integer() else str(value)


def main(argv=None):
    arguments = sys.argv[1:] if argv is None else argv
    result = sum_from_argv(arguments)
    print(format_number(result))
    return result


if __name__ == "__main__":
    main()
