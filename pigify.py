import os
import re

def is_capital(component):
    # returns either "capitalized" or "lower"
    capitals = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    lowers = 'qwertyuiopasdfghjklzxcvbnm'
    type = ''
    if component[0] in capitals:
        type = 'capitalized'
    elif component[0] in lowers:
        type = 'lower'
    return type

def pig_lat(englishWord):
    if len(englishWord) == 0:
        return None
    vowel_list = 'aeiou'
    consonant_list = 'bcdfghjklmnpqrstvwxyz'
    pigLatinWord = ''
    if englishWord[0] in vowel_list:
        pigLatinWord = englishWord + 'way'
    else:
        if (englishWord[0] in consonant_list) and (len(englishWord) >= 2):
            if (englishWord [1] in consonant_list) and (len(englishWord) >= 3):
                if (englishWord[2] in consonant_list):
                    pigLatinWord = englishWord[3:]+englishWord[:3]+'ay'
                else:
                    pigLatinWord = englishWord[2:]+englishWord[:2]+'ay'
            else:
                pigLatinWord = englishWord[1:]+englishWord[:1]+'ay'
    return pigLatinWord

for file in os.listdir('eng_txts'):
    f = open('eng_txts/' + file,'r')
    eng_string = f.read()
    f.close()
    eng_list = re.findall(r"[\w']+|[\n]+|[ ]+|[_.,!?;]", eng_string, re.UNICODE)
    #print(eng_list)

    letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    output_text = ''
    pig_lat_word = ''
    word = ''
    capitalization = ''

    for component in eng_list:
        if component[0] not in letters:
            output_text = output_text + component
            #print('adding punct or whitespace or something')

        else:
            #print('adding a word')
            capitalization = is_capital(component)
            word = component.lower() # this does not modify component
            pig_lat_word = pig_lat(word)
            if capitalization=='capitalized':
                pig_lat_word = pig_lat_word.capitalize()
            output_text = output_text + pig_lat_word
    with open('pig_lat_txts/' + file[:-4] + '_in_Pig_Latin.txt','w') as f:
        f.write(output_text)
