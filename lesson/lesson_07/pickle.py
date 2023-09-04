import json

star_string = '[{"name": "Python", "typing": "Dynamic", "reflection": }]'

languages = json.loads(star_string)
print(languages, type(languages))

p = ProgrammingLanguage()

json_string = json.dumps(languages, default=vars)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 19)