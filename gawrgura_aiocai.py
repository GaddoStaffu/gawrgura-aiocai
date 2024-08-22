from characterai import aiocai
import asyncio
import pyttsx3

engine = pyttsx3.init()

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female



gawr_says = "Did not Change"

def ai_convo():
    return gawr_says



async def talktoai():
    global gawr_says

    char = "oL2IzOD15_wBIP_o6NAWDwiVyAnzz_3aGLu9aU7i254"

    client = aiocai.Client('ceaf8e69970f170b9166c733f377201a9510a608')

    me = await client.get_me()

    async with await client.connect() as chat:
        new, answer = await chat.new_chat(
            char, me.id
        )

        print(f'{answer.name}: {answer.text}')
        
        while True:
            text = input('YOU: ')
            
            if text.lower() in ["cm_exit"]:
                print("Ending conversation...")
                break
            message = await chat.send_message(
                char, new.chat_id, text
            )

            print(f'{message.name}: {message.text}')
            gawr_says = (message.text)
            engine.say(message.text)
            engine.runAndWait()
        engine.stop()




