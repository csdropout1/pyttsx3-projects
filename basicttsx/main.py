import pyttsx4

'''
Run the program with tts.list_voices() uncommented to determine your voice IDs
If you have a mac like me, the defaults should work!

As of November 1, 2023, pyttsx4 is not merged with the most recent update of python. Please add the line 
'import objc' in the nsss.py. You will know what I mean when you attempt to run this file and it throws an error!
'''

chn = 'com.apple.voice.compact.zh-CN.Tingting'
krn = 'com.apple.voice.compact.ko-KR.Yuna'
jpn = 'com.apple.voice.compact.ja-JP.Kyoko'

class TextToSpeech:
    def __init__(self, voice, rate, volume):
        self.engine = pyttsx4.init()
        # voices = self.engine.getProperty('voices')
        if voice:
            self.engine.setProperty('voice', voice)
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

    def list_voices(self):
        voices = self.engine.getProperty('voices')

        for i, voice in enumerate(voices):
            print(f'{i + 1} {voice.name} {voice.age} {voice.languages[0]} {voice.gender} {voice.id}')

    def text_to_speech(self, text, save = False, file_name = 'output.mp3'):
        self.engine.say(text)
        print('I am speaking ...')

        if save:
            self.engine.save_to_file(text, file_name)
        
        self.engine.runAndWait()

if __name__ == '__main__':
    tts = TextToSpeech(jpn, 200, 1.0)
    # tts.list_voices()
    # tts.text_to_speech('Time to Make some Youtube Videos')

 





