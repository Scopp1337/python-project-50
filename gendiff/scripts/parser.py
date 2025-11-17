import json
import os


def get_file_format(file_path):
    _, extension = os.path.splitext(file_path)
    return extension[1:]


def read_file(file_path):
    with open(file_path, encoding='utf-8') as file:
        return file.read()


def parse_data(data, format):
    if format == 'json':
        return json.loads(data)
    raise ValueError(f'Unsupported file format: {format}')


def parse_data_from_file(file_path):
    data = read_file(file_path)
    format = get_file_format(file_path)
    return parse_data(data, format)