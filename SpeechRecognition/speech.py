import speech_recognition as sr
import subprocess
import datetime
import pyowm
import webbrowser
recognizer = sr.Recognizer()
owm = pyowm.OWM("5817d6a145c443107efc34417e35c2ac")
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
        

    elif "калькулятор" in text.lower():
        subprocess.call(["calc"])

    elif "погода" in text.lower():
        place = text.lower()[7:]

        observation = owm.weather_manager().weather_at_place(place)
        location = observation.location
        weather = observation.weather
        weather = "Температура (градусів Цельсію):" + str(int(weather.temperature("celsius")["temp"]))
        print(weather)
    elif 'час' in text:
        now = datetime.datetime.now()
        print(now)
    # elif "яка погода" in text: 
    #     print("Сьогодні сонячно з температурою близько 25 градусів.")
    elif "хочу поработать" in text.lower():
        subprocess.call([r"C:\Users\LOGIKA\AppData\Local\Programs\Microsoft VS Code\Code.exe"])

    elif "хром" in text.lower():
        subprocess.call(["C:\Program Files\Google\Chrome\Application\chrome.exe"])
    elif "логіка" in text.lower():
        webbrowser.open("https://student.logikaschool.com.ua/dashboard?=1757169622623")
    
    elif "youtube" in text.lower():
        webbrowser.open(f"https://www.youtube.com/results?search_query={text.lower()[7:]}")
        

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