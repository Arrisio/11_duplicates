import os
from collections import Counter, defaultdict
import argparse


def find_duplicates(directory):
    files_counter = Counter()
    files_locations = defaultdict(list)
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            files_counter[(file, file_size)] += 1
            files_locations[(file, file_size)].append(file_path)

    return {
        file_idx: files_locations[file_idx]
        for file_idx in files_counter if files_counter[file_idx] > 1
    }


def print_duplicates(duplicates_list):
    if duplicates_list:
        for (file_name, file_size), paths_list in duplicates_list.items():
            print('File: {}, size: {}'.format(file_name, file_size))
            for path in paths_list:
                print(path)
    else:
        print('No duplicates found')


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-d', action='store',
        dest='directory',
        help='directory to find duplicates',
        default='.'
    )

    return parser.parse_args()


if __name__ == '__main__':
    params = parse_arguments()

    duplicates_list = find_duplicates(params.directory)
    print_duplicates(duplicates_list)
