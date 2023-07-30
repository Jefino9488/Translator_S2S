# machine learning test
from translator import Translator  # Import the Translator class from the translator module

text = input("Enter a sentence to translate: ")
target_lang = input("Enter the target language: ")

while text != "bye":
    try:
        translator = Translator(text, target_lang)  # Create an instance of the Translator class
        translation = translator.offline_translator.translate_offline(text,target_lang)
        print(translation)
    except Exception as e:
        print("An error occurred:", str(e))
        print("Please try again...")

    text = input("Enter a sentence to translate: ")
    target_lang = input("Enter the target language: ")
