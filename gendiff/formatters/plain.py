def format_value(value):
    if isinstance(value, (list, dict)):
        return '[complex value]'
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def make_plain_item(item, path=''):
    key = item.get('name')
    action = item.get('action')
    new_val = format_value(item.get('new_value'))
    old_val = format_value(item.get('old_value'))
    cur_path = f"{path}.{key}" if path else key

    if action == 'added':
        return f"Property '{cur_path}' was added with value: {new_val}"
    if action == 'deleted':
        return f"Property '{cur_path}' was removed"
    if action == 'modified':
        return f"Property '{cur_path}' was updated. From {old_val} to {new_val}"
    if action == 'nested':
        return make_plain_diff(item.get('children'), cur_path)
    return None


def make_plain_diff(diff, path=''):
    result = []
    for item in diff:
        formatted_item = make_plain_item(item, path)
        if formatted_item is not None:
            result.append(formatted_item)

    return '\n'.join(result)


def format_diff_plain(diff):
    return make_plain_diff(diff)

