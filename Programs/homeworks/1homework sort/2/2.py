import re

lines = ['аист', 'Юла', 'Call', 'string', 'Олег', 'box', 'Улий']

for line in lines:
    if re.match(r'\b[аяуюоеёэиы][а-яa-z]*\b', line, re.IGNORECASE):
        print(line)