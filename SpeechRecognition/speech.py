import speech_recognition as sr

recognizer = sr.Recognizer()

def capture_voice(): # захоплення голосу
    with sr.Microphone() as source: # використання мікрофона як джерела
        print("слушаю") # повідомлення користувачу
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=10) # прослуховування джерела
    return audio # повернення аудіо

def convert_to_text(audio): # конвертація голосу в текст
    try:
        text = recognizer.recognize_google(audio, language="uk-UA") # розпізнавання голосу
        print("ви сказали:" + text) # виведення розпізнаного тексту
    except:
        text = "" # якщо не вдалося розпізнати
        print("не вдалося розпізнати") 
    return text # повернення тексту

def process_voice_command(text): # обробка голосової команди
    text = text.lower() # приведення тексту до нижнього регістру
    if 'привіт' in text: # перевірка на привітання
        print("Привіт як я можу допомогти?") 
    elif 'прощавай' in text:
        print("До побачення! Гарного дня!")
        return True # завершення програми
    elif "яка погода" in text: 
        print("Сьогодні сонячно з температурою близько 25 градусів.")
    elif "хто ти" in text:
        print("Я голосовий помічник створений для допомоги вам.")
    else:
        print("Вибачте я не розумію цю команду")
    return False # продовження програми

def main():
    end_program = False # змінна для завершення програми
    while not end_program: 
        audio = capture_voice() # захоплення голосу
        text = convert_to_text(audio) # конвертація в текст
        end_program = process_voice_command(text) # обробка команди

if __name__ == "__main__":
    main()