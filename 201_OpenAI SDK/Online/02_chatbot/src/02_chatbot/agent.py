import chainlit as cl

import os
from agents import Agent, RunConfig, OpenAIChatCompletionsModel, Runner
from openai import AsyncOpenAI
from dotenv import load_dotenv, find_dotenv
import asyncio

load_dotenv(find_dotenv())

# Try to get the API key from environment variables
gemini_api_key = os.getenv("GOOGLE_API_KEY")

# Check if API key is available
if not gemini_api_key:
    print("Error: GOOGLE_API_KEY environment variable is not set.")
    print("Please set your Google API key in one of the following ways:")
    print("1. Create a .env file with: GOOGLE_API_KEY=your_api_key_here")
    print("2. Set the environment variable: export GOOGLE_API_KEY=your_api_key_here")
    print("3. Set it in your system environment variables")
    exit(1)

# Step 1: Provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Step 2: Model
model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=provider,
)

# Config at Run level
run_config = RunConfig(
    model=model,
    tracing_disabled=True,
)

# Step 3: Agent
agent1 = Agent(
    name="gemini_agent",
)

# # Step 4: Run
# result = Runner.run_sync(
#     agent1,
#     "What is the capital of Australia?",
#     run_config=run_config,
# )

# print(result.final_output)


@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(content="I'm Hasnain's Agent, how can I help you today?").send()


@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history", [])

    msg = cl.Message(content="")
    await msg.send()
    
    # Ensure history is always a list
    if history is None:
        history = []

    # Add the current user message to history
    history.append({"role": "user", "content": message.content})

    # Format the conversation history for the LLM
    conversation_context = ""
    if len(history) > 1:  # If there's previous conversation
        conversation_context = "Previous conversation:\n"
        for msg in history[:-1]:  # All messages except the current one
            role = "User" if msg["role"] == "user" else "Assistant"
            conversation_context += f"{role}: {msg['content']}\n"
        conversation_context += "\nCurrent message: "
    
    # Create the full input with context
    full_input = conversation_context + message.content if conversation_context else message.content

    # Run the agent with the full context using sync method
    result = Runner.run_sync(
        agent1,
        full_input,
        run_config=run_config,
    )
    
    # Simulate streaming by sending the response in chunks
    response_text = result.final_output
    chunk_size = 10  # Send 10 characters at a time
    
    for i in range(0, len(response_text), chunk_size):
        chunk = response_text[i:i + chunk_size]
        await msg.stream_token(chunk)
        await asyncio.sleep(0.05)  # Small delay to simulate streaming

    # Add the assistant's response to history
    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)
