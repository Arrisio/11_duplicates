import os
from collections import defaultdict
import argparse


def find_duplicates(directory):
    files_locations = defaultdict(list)
    for root, _, file_names in os.walk(directory):
        for file_name in file_names:
            file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(file_path)
            files_locations[(file_name, file_size)].append(file_path)

    return {
        file_idx: file_paths
        for file_idx, file_paths in files_locations.items()
        if len(file_paths) > 1
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
