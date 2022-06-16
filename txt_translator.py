'''
make a txt translator
'''
from translate import Translator

translator = Translator(to_lang='ja')

with open('text.txt') as myfile:
    text = myfile.read()
    translation = translator.translate(text)
    print(text)
    print(translation)

with open('translated_text.txt', mode='w', encoding='utf-8') as newfile:
     newfile.write(translation)



