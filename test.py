# Don't forget to install watson packages with Pip
import sys
import json
from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator

class Translate:

    input_language = ""
    output_language = ""
    models = []
    translator = ""


    #Loads credentials from a file and creates the translator
    def load_credentials(self, file_name):
        print(file_name)
        with open(file_name) as data_file:
            creds = json.loads(data_file.read())
        self.translator = LanguageTranslator(
            username=creds["translate_username"],
            password=creds["translate_password"])
        self.models = self.translator.get_models()["models"]


    #TODO Edit this method mostly
    def startTranslation(self):
        print(self.list_languages())

    #Lists the languages as a string
    #FIXME should really return a set
    def list_languages(self):
        temp = ""
        for model in self.models:
            temp = temp+model['source']+" "
        return temp
        
    def __init__(self, credential_file):
        self.load_credentials(credential_file)
        self.startTranslation()

#Entry point
if len(sys.argv)>1:
    Translate(sys.argv[1])
else:
    Translate("credentials.json")
