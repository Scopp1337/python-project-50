from gendiff.formatters.json_formatter import format_diff_json
from gendiff.formatters.plain import format_diff_plain
from gendiff.formatters.stylish import format_diff_stylish


def format_identifier(diff, formatter):
    match formatter:
        case 'stylish':
            return format_diff_stylish(diff)
        case 'plain':
            return format_diff_plain(diff)
        case 'json':
            return format_diff_json(diff)
        case _:
            raise ValueError(f"Unsupported formatter: {formatter}")