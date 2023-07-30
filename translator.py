# translator main class
from googletrans import Translator as GoogleTranslator
from gtts import gTTS
from pydub import AudioSegment
import speech_recognition as sr
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast


class Translator:
    def __init__(self, text, target_lang):
        self.user_input = text
        self.target_lang = target_lang
        self.tts = gTTS(text=self.user_input, lang="en", slow=False, lang_check=True)
        self.online_translator = self.OnlineTrans(text)
        self.offline_translator = self.OfflineTrans()

    class OnlineTrans:
        def __init__(self, text):
            self.user_input = text
            self.translator = GoogleTranslator()
            self.tts = gTTS(text=self.user_input, lang="en", slow=False, lang_check=True)

        def translate_online(self, text, target_lang):
            result = self.translator.translate(text, dest=target_lang)
            return result.text

        def text_to_speech(self, text, lang):
            try:
                self.tts = gTTS(text=text, lang=lang, slow=False, lang_check=True)
                self.tts.save("audio.mp3")
                audio = AudioSegment.from_file("audio.mp3", format="mp3")
                return audio
            except ValueError as e:
                print(f"An error occurred: {e}")

    class OfflineTrans:
        def __init__(self):
            self.model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
            self.tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-one-to-many-mmt",
                                                                  src_lang="en_XX")

        def translate_offline(self, text, target_lang):
            model_inputs = self.tokenizer(text, return_tensors="pt")
            generated_tokens = self.model.generate(
                **model_inputs,
                forced_bos_token_id=self.tokenizer.lang_code_to_id["{}".format(target_lang)], max_new_tokens=1000)
            translation = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
            return translation[0]
