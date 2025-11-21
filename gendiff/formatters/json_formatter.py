import json


def format_diff_json(diff):
    return json.dumps(diff, indent=2, ensure_ascii=False)