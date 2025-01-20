from characterai import aiocai
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

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

    try:
        char = "oL2IzOD15_wBIP_o6NAWDwiVyAnzz_3aGLu9aU7i254"
        client = aiocai.Client('ceaf8e69970f170b9166c733f377201a9510a608')

        me = await client.get_me()
        async with await client.connect() as chat:
            new, answer = await chat.new_chat(char, me.id)
            print(f'{answer.name}: {answer.text}')
            
            while True:
                text = input('YOU: ')
                if text.lower() in ["cmd_exit"]:
                    print("Ending conversation...")
                    break
                message = await chat.send_message(char, new.chat_id, text)
                print(f'{message.name}: {message.text}')
                
                # Update the message and speak it out
                gawr_says = message.text
                engine.say(gawr_says)
                engine.runAndWait()

        engine.stop()  # Ensure the engine stops after the conversation

    except Exception as e:
        print(f"An error occurred: {e}")
        engine.stop()  # Stop the engine if an error occurs
