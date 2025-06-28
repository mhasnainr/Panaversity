import chainlit as cl

from agents import Agent, RunConfig, OpenAIChatCompletionsModel, Runner
from openai import AsyncOpenAI
from .config import get_config

# Get configuration
config = get_config()

# Validate configuration on startup
if not config.validate():
    print("Configuration Error:")
    print(config.get_setup_instructions())
    exit(1)

# Step 1: Provider
provider = AsyncOpenAI(
    api_key=config.google_api_key,
    base_url=config.base_url,
)

# Step 2: Model
model = OpenAIChatCompletionsModel(
    model=config.model_name,
    openai_client=provider,
)

# Config at Run level
run_config = RunConfig(
    model=model,
    tracing_disabled=not config.debug,
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

    # Run the agent with the full context
    result = await Runner.run(
        agent1,
        input=full_input,
        run_config=run_config,
    )

    # Add the assistant's response to history
    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)
    
    await cl.Message(
        content=result.final_output
    ).send()
