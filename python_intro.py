# girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']



# def hi(name):
#     print('Hi ' + name + '!')

# girls = ['Rachel', 'Phoebe', 'Ola', 'You']

# for name in girls:
#     hi(name)
#     print('Next girl')
#     print('ok')


known_languages = ['English']
unknown_languages = ['Spanish', 'German']

def myfunction(language, other):
    print("I " + other + " " + language)

for language in known_languages:
    myfunction(language, 'know')

for language in unknown_languages:
    myfunction(language, 'don\'t know')

# I know "English"
# I know "Spanish"
# I know "German"