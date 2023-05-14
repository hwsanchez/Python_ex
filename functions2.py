#Example of a Function with a parameter AND a return
#we use the def keyword to define a function
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

name = input('Enter your name: ')
language = input('Enter a language(en = English, es = Espanol, fr = Francois): ')
print(greet(language), name)
