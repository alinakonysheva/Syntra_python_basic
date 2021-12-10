C_FILE = 'test.json'


def create_json_file(contents: str):
    try:
        with open(C_FILE, 'w') as f:
            f.write(contents)
    except Exception as e:
        print(f'create_json_file: {e}')
        return False

    return True


def read_json_file() -> str:
    contents = ''
    try:
        with open(C_FILE, 'r') as f:
            contents = str(f.read())
    except Exception as e:
        print('create_json_file: {}'.format(e))

    return contents
