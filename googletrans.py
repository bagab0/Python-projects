import speech_recognition as sr
import pyttsx3
from googletrans import Translator

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function for the AI assistant to speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize and return speech input
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
        return query
    except Exception as e:
        print("Sorry, I couldn't understand that.")
        return None

# Translator function
def translate_text(text, target_language="fr"):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

# Main AI assistant function
def ai_assistant():
    speak("Hello! I am your language assistant. How can I help you?")
    while True:
        query = recognize_speech()
        if query is None:
            continue

        # Basic AI responses
        if "hello" in query.lower():
            response = "Hi there! How can I assist you today?"
            print(response)
            speak(response)
        elif "how are you" in query.lower():
            response = "I'm doing well, thank you for asking! What would you like to translate today?"
            print(response)
            speak(response)
        elif "translate" in query.lower():
            speak("Please tell me the sentence you'd like to translate.")
            sentence = recognize_speech()
            if sentence:
                translation = translate_text(sentence, target_language="fr")
                print(f"Translation: {translation}")
                speak(f"The translation is: {translation}")
        elif "stop" in query.lower() or "exit" in query.lower():
            speak("Goodbye! Have a great day.")
            break
        else:
            speak("I'm sorry, I didn't catch that. Can you please repeat?")

# Start the assistant
ai_assistant()
