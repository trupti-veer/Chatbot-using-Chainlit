import chainlit as cl

from src.messenger import ask_order, messages

@cl.on_message
async def main(message: cl.Message):
    
    messages.append({"role": "user", "content": message.content})
    response = ask_order(messages)
    messages.append({"role": "assistant", "content": response})

    # Send a response back to the user
    await cl.Message(
        content=response,
    ).send()