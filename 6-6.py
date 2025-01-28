people = ['arturo', 'vidal', 'francisco','phil','edward']

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python' 
}

for person in people:
    if person in favorite_languages.keys():
        print(f"{person}, Thanks for responding the poll.")
    else:
        print(f"{person}, Please take the poll.")
