'''
This is the tranlator module, which connects to IBM Language Translator
and returns a string in a different language (EN to FR or FR to EN)
'''
#import json
import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
#language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    """This translates english_text from English to French using IBM Language Translator"""
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
    french_text=translation["translations"][0]["translation"]
    return french_text

def french_to_english(french_text):
    """This translates french_text from French to English using IBM Language Translator"""
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
    english_text=translation["translations"][0]["translation"]
    return english_text


#print(json.dumps(translation, indent=2, ensure_ascii=False))
