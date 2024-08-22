from characterai import aiocai
import asyncio


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




