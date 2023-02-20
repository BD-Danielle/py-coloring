import requests
import json
from wordSaved import wordSaved
# 定義API的網址
word = "lucid"
url = "https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(word)

# 呼叫API並獲取數據
response = requests.get(url)

# 將數據轉換為json格式
data = json.dumps(response.text)

# 使用數據進行運算或顯示
# print(data)
wordSaved(word, data)