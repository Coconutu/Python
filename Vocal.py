import speech_recognition as sr
def Asculta_si_scrie(timp):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # citeste informatia audio de la microfonul implicit
        try:

            audio_data = r.record(source, duration=timp)
            # transforma audio in text
            text = r.recognize_google(audio_data, language="ro-RO")
            return text
        except:
            pass

