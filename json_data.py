import requests
import json

url = 'http://169.254.169.254/latest/'


def gather_information(url, arr):
    output = {}
    for i in arr:
        url1 = url + i
        re = requests.get(url1)
        text = re.text
        if i[-1] == "/":
            value = re.text.splitlines()
            output[i[:-1]] = gather_information(url1, value)
        elif is_json(text):
            output[i] = json.loads(text)
        else:
            output[i] = text
    return output


def get_data():
    initial = ["meta-data/"]
    information = gather_information(url, initial)
    return information


def get_json():
    data = get_data()
    json_output = json.dumps(data, indent=4, sort_keys=True)
    return json_output


def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    print(get_json())