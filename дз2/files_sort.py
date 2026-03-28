import os
import sys


def sort_files_by_extension(directory):
    files = [
        entry
        for entry in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, entry))
    ]
    return sorted(files, key=lambda name: (os.path.splitext(name)[1], name))


def main(argv=None):
    arguments = sys.argv[1:] if argv is None else argv
    if not arguments:
        return []

    sorted_files = sort_files_by_extension(arguments[0])
    for filename in sorted_files:
        print(filename)
    return sorted_files


if __name__ == "__main__":
    main()
