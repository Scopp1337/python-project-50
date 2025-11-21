SEPARATOR = " "
ADD = '+ '
DEL = '- '
NONE = '  '


def format_value(value, spaces_count=2):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        indent = SEPARATOR * (spaces_count + 4)
        result_lines = []
        for key, inner_value in value.items():
            formatted_value = format_value(inner_value, spaces_count + 4)
            result_lines.append(f"{indent}{NONE}{key}: {formatted_value}")
        formatted_string = '\n'.join(result_lines)
        end_indent = SEPARATOR * (spaces_count + 2)
        return f"{{\n{formatted_string}\n{end_indent}}}"
    if value == "":
        return ""

    return str(value)


def make_stylish_diff(diff, spaces_count=2):
    indent = SEPARATOR * spaces_count
    lines = []

    for item in diff:
        key = item['name']
        action = item['action']
        value = item.get('value')
        old_value = item.get('old_value')
        new_value = item.get('new_value')

        match action:
            case "unchanged":
                formatted_value = format_value(value, spaces_count)
                line = f"{indent}{NONE}{key}: {formatted_value}"
                lines.append(line)

            case "modified":
                formatted_old = format_value(old_value, spaces_count)
                formatted_new = format_value(new_value, spaces_count)

                if old_value == "":
                    old_line = f"{indent}{DEL}{key}: "
                else:
                    old_line = f"{indent}{DEL}{key}: {formatted_old}"

                new_line = f"{indent}{ADD}{key}: {formatted_new}"
                lines.extend([old_line, new_line])

            case "deleted":
                formatted_old = format_value(old_value, spaces_count)
                if old_value == "":
                    line = f"{indent}{DEL}{key}: "
                else:
                    line = f"{indent}{DEL}{key}: {formatted_old}"
                lines.append(line)

            case "added":
                formatted_new = format_value(new_value, spaces_count)
                line = f"{indent}{ADD}{key}: {formatted_new}"
                lines.append(line)

            case "nested":
                children = make_stylish_diff(
                    item.get("children"), spaces_count + 4
                )
                line = f"{indent}{NONE}{key}: {children}"
                lines.append(line)

    formatted_string = '\n'.join(lines)
    end_indent = SEPARATOR * (spaces_count - 2)
    return f"{{\n{formatted_string}\n{end_indent}}}"


def format_diff_stylish(data):
    return make_stylish_diff(data)