"""This programs executes translation from english to french and viceversa."""
import json
import os
import re
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-11-29',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(englishtext):
    """ This function translates english to french"""
    #write the code here
    if englishtext=="":
        return ""
    translation = language_translator.translate(
    text=englishtext,
    model_id='en-fr').get_result()
    frenchtext = json.dumps(translation, indent=2, ensure_ascii=False)
    frenchtext = re.search(r"([translation]*\"): \"([\w+ ]*)\"",frenchtext)
    return frenchtext[2]
    
def french_to_english(frenchtext):
    """ This function translates french to english"""
    #write the code here
    if frenchtext == "":
        return ""
    translation = language_translator.translate(
    text=frenchtext,
    model_id='fr-en').get_result()
    englishtext = json.dumps(translation, indent=2, ensure_ascii=False)
    englishtext = re.search(r"([translation]*\"): \"([\w+ ]*)\"",englishtext)
    return englishtext[2]

