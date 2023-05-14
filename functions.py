#Introduction to functions in Python
#First Example: with a parameter and without a return
def greet(lang):
    if lang == 'es':
        print('Hola!')
    elif lang == 'fr':
        print('Bonjour!')
    elif lang == 'en':
        print('Hello!')
    else:
        print('Invalid Language!')
language = input('Choose a Language (en = Engilsh, es = Espanol, fr = francois): ')
greet(language)
