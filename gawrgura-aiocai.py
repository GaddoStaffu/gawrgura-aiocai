from characterai import aiocai
import asyncio

ai_chat = "Starting"

async def main():
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

            message = await chat.send_message(
                char, new.chat_id, text
            )

            print(f'{message.name}: {message.text}')
            ai_chat = message.text


asyncio.run(main())

