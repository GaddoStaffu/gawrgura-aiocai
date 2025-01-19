import asyncio
import gawrgura_aiocai

print("Waking up Gawr Gura....")

# Run the asynchronous function using asyncio
try:
    asyncio.run(gawrgura_aiocai.talktoai())
except Exception as e:
    print(f"An error occurred: {e}")
