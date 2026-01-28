import requests, json
from wordSaved import word_saved
from withOpen import with_open_write

# with_open_read

word = "lucid"

# call api and get data


def callAPI(word):
    if not (word_saved(word)):
        url = "https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(word)
        response = requests.get(url)
        data = json.dumps(json.loads(response.text), indent=2, ensure_ascii=False)
        with_open_write(word, 'json', 'utf-8', data)
    else:
        print('api not called')


callAPI(word)
