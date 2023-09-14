import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Say something:")
    # Adjust for ambient noise
    recognizer.adjust_for_ambient_noise(source)
    # Listen to the user's input
    audio = recognizer.listen(source)

    try:
        # Recognize the speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
