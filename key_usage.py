from json_data import get_data



def gen_dict_extract(key, var):
    if hasattr(var, 'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in gen_dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(key, d):
                        yield result


def find_key(key):
    data = get_data()
    return list(gen_dict_extract(key, data))


if __name__ == '__main__':
    key = input("What key would you like to find?\n")
    print(find_key(key))