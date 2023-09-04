import json
import requests

URL = 'https://api.github.com/repos/CP1404/demo/demos/issues'

response = requests.get(URL)
text = response.json()
print(type(text))

demo_text = """{
    "number": 1,
    "title": "Demo",
    "state": "open"
}"""

thing = json.loads(demo_text)
print(thing)
print(type(thing))
print(thing['title'])
thing['title'] = thing['title'].upper()
print(thing['title'])

text = json.dumps(thing)
print()
print(type(text))
