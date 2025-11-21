def item_add(key, value):
    return {
        'action': 'added',
        'name': key,
        'new_value': value
    }


def item_delete(key, value):
    return {
        'action': 'deleted',
        'name': key,
        'old_value': value
    }


def items_unchanged(key, value):
    return {
        'action': 'unchanged',
        'name': key,
        'value': value
    }


def items_modified(key, value1, value2):
    return {
        'action': 'modified',
        'name': key,
        'new_value': value2,
        'old_value': value1
    }


def items_nested(key, value1, value2):
    return {
        'action': 'nested',
        'name': key,
        'children': find_diff(value1, value2)
    }


def find_diff(data1, data2):
    diff = []

    for key in sorted(data1.keys() | data2.keys()):
        value1 = data1.get(key)
        value2 = data2.get(key)

        match (key in data1, key in data2):
            case (False, True):
                diff.append(item_add(key, value2))
            case (True, False):
                diff.append(item_delete(key, value1))
            case (True, True) if (
                    isinstance(value1, dict) and
                    isinstance(value2, dict)
            ):
                diff.append(items_nested(key, value1, value2))
            case (True, True) if value1 != value2:
                diff.append(items_modified(key, value1, value2))
            case _:
                diff.append(items_unchanged(key, value1))

    return diff