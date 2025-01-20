from characterai import aiocai
import pyttsx3
import speech_recognition as sr
# Initialize the text-to-speech engine
engine = pyttsx3.init()
r = sr.Recognizer()
# Set up the voice properties
def setup_voice():
    """Setup voice rate, volume, and voice type."""
    rate = engine.getProperty('rate')
    print(f"Current rate: {rate}")
    engine.setProperty('rate', 125)  # Adjust speaking rate
    volume = engine.getProperty('volume')
    print(f"Current volume: {volume}")
    engine.setProperty('volume', 1.0)  # Set volume to maximum
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Use female voice

# Function to start the AI conversation
async def talktoai():
    setup_voice()
    gawr_says = "Did not Change"  # Default message

    try:
        char = "oL2IzOD15_wBIP_o6NAWDwiVyAnzz_3aGLu9aU7i254"
        client = aiocai.Client('ceaf8e69970f170b9166c733f377201a9510a608')

        me = await client.get_me()
        async with await client.connect() as chat:
            new, answer = await chat.new_chat(char, me.id)
            print(f'{answer.name}: {answer.text}')
            
            while True:
                print("Listening.....")
                userreply = talk()
                print(f'You Said: {userreply}')
                message = await chat.send_message(char, new.chat_id, userreply) # message text to talk to character 
                print(f'{message.name}: {message.text}')

                
                # Update the message and speak it out
                gawr_says = message.text
                engine.say(gawr_says) # calling a tts library to say the message
                engine.runAndWait() # wait for the tts to finish talking to continue

        engine.stop()  # Ensure the engine stops after the conversation

    except Exception as e:
        print(f"An error occurred: {e}")
        engine.stop()  # Stop the engine if an error occurs



def talk()->str:
    while(1):

        # Exception handling to handle
        # exceptions at the runtime
        try:

            # use the microphone as source for input.
            with sr.Microphone() as source2:
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)
                #listens for the user's input
                audio2 = r.listen(source2)
                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                
                return MyText

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("Sorry, can you repeat that?")