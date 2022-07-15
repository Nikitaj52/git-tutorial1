import speech_recognition
import webbrowser
import wikipedia
UserVoiceRecognizer = speech_recognition.Recognizer()
while(1):
    try:
        with speech_recognition.Microphone() as UserVoiceInputSource:
 
            UserVoiceRecognizer.adjust_for_ambient_noise(UserVoiceInputSource, duration=0.5)
 
            # The Program listens to the user voice input.
            print("Listening......")
            UserVoiceInput = UserVoiceRecognizer.listen(UserVoiceInputSource)
 
            UserVoiceInput_converted_to_Text = UserVoiceRecognizer.recognize_google(UserVoiceInput)
            UserVoiceInput_converted_to_Text = UserVoiceInput_converted_to_Text.lower()
            print(UserVoiceInput_converted_to_Text)
            if UserVoiceInput_converted_to_Text in ['google','youtube','yahoo','gmail']:
                webbrowser.open(UserVoiceInput_converted_to_Text+".com")
            
            else:
                wikipedia.set_lang("hi")
                data=wikipedia.summary(UserVoiceInput_converted_to_Text, sentences=10)
                print(data)
                file1 = open("myfile.txt", "a")
                print(file1,"myfile.txt")
                file1.writelines(data)
                file1.close()
                
    except KeyboardInterrupt: 
        print('A KeyboardInterrupt encountered; Terminating the Program !!!')
        exit(0)
    except speech_recognition.UnknownValueError:
        print("No User Voice detected OR unintelligible noises detected OR the recognized audio cannot be matched to text !!!")
        