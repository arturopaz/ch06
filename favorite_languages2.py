favorite_languages = {
    'jen' : ['python','rust'],
    'sarah' : ['c'],
    'edward': ['rust','go'],
    'phil' : ['python','haskell'],
}

for person,languages in favorite_languages.items():
    print(f"\nA {person.title()} le gustan los siguientes lenguajes de programación:")
    for language in languages:
        print(f"\t{language.title()}")
