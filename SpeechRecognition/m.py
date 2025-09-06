import speech_recognition as sr

recognizer = sr.Recognizer()

def capture_voice(): 
    with sr.Microphone(device_index=5) as source:  # 👈 указываем card 1
        print("Слухаю...")
        audio = recognizer.listen(source)
    return audio

def convert_to_text(audio):
    try:
        text = recognizer.recognize_google(audio, language="uk-UA")
        print("Ви сказали: " + text)
    except:
        text = ""
        print("Не вдалося розпізнати")
    return text

def process_voice_command(text):
    text = text.lower()
    if 'привіт' in text:
        print("Привіт, як я можу допомогти?")
    elif 'прощавай' in text:
        print("До побачення! Гарного дня!")
        return True
    elif "яка погода" in text:
        print("Сьогодні сонячно з температурою близько 25 градусів.")
    elif "хто ти" in text:
        print("Я голосовий помічник, створений для допомоги вам.")
    else:
        print("Вибачте, я не розумію цю команду.")
    return False

def main():
    end_program = False
    while not end_program:
        audio = capture_voice()
        text = convert_to_text(audio)
        end_program = process_voice_command(text)

if __name__ == "__main__":
    main()
