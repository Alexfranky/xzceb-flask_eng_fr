"""importing neccessary libraries, modules and packages"""
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
API_KEY = ""
URL= ""

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
language_translator.set_service_url(URL)

def english_to_french(english_text):

    """This function translates a text from english to french"""
    translate= language_translator.translate(text= english_text, model_id="en-fr").get_result()
    french_text = translate['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    """This function translates a text from french to english"""
    translate = language_translator.translate(text=french_text, model_id="fr-en").get_result()
    english_text = translate['translations'][0]['translation']
    return english_text # TO be added
