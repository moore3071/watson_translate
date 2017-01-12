# python 2.7
# pip install --upgrade watson-developer-cloud
# Connor Wood & Brandon Moore

import json
from watson_developer_cloud import LanguageTranslatorV2 as LanguageTranslator

language_translator = LanguageTranslator(
    username='236bcdc1-2403-41d3-8ebd-c760f6782209',
    password='tai3d3r7d6QY')

#languages = language_translator.get_identifiable_languages()
#print(json.dumps(languages, indent=2))

def language_select():
	print("1) Arabic")
	print("2) German")
	print("3) French")
	print("4) Chinese")
	print("")

	user_input = input('Select a language to translate to from above: ')
	switcher = {
		1: "ar",
		2: "de",
		3: "fr",
		4: "zh"
	}
	return switcher.get(user_input, "error")

def user_prompt():
	return raw_input("Enter some text to be translated: ")

def translate(language, text):
	translation = language_translator.translate(
    text=text,
    source='en',
    target=language)
	return json.dumps(translation, indent=2, ensure_ascii=False)


def main():
	translateAgain =  True
	print('\nWelcome to our language translator! Powered by IBM Watson \n')
	language = language_select()
	while(translateAgain):
		text = user_prompt()
		newText = translate(language, text)

		print(newText)

		Userinput = input('Translate more (1 : YES, 0 : NO): ')
		translateAgain = True if Userinput==1 else False

main()