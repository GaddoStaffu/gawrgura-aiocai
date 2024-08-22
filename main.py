import asyncio
import gawrgura_aiocai
import pyttsx3

print("Waking up Gawr Gura....")

# Run the asynchronous function using asyncio
asyncio.run(gawrgura_aiocai.talktoai())

# Print the final response from Gawr Gura
print(gawrgura_aiocai.gawr_says)

print()