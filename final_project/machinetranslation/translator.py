"""deep translator module imports"""
from deep_translator import MyMemoryTranslator

'''this module will translate to french'''
def englishtofrench(englishtext):
    '''english'''
    frenchtext = MyMemoryTranslator(source='en-GB', target='fr-FR').translate(englishtext)
    return frenchtext

'''french to english translation'''
def frenchtoenglish(frenchtext):
    '''french'''
    englishtext = MyMemoryTranslator(source='fr-FR', target='en-GB').translate(frenchtext)
    return englishtext
