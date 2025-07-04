import os
from agents import Agent, Runner, set_tracing_disabled, set_default_openai_api
from agents.run import RunConfig
from agents import OpenAIChatCompletionsModel
from agents.models.openai_provider import OpenAIProvider
from dotenv import load_dotenv
from pathlib import Path
from openai import AsyncOpenAI

load_dotenv(dotenv_path=Path(".venv") / ".env")

GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set.")

# Set the default OpenAI API to chat_completions (string, not client)
set_default_openai_api("chat_completions")

openai_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=openai_client,
)

config = RunConfig(
    model=model,
    model_provider=OpenAIProvider(
        api_key=GEMINI_API_KEY, base_url="https://generativelanguage.googleapis.com/v1beta/openai/"),
)

agent = Agent(name="Assistant",
              instructions="You are a helpful assistant",
              model=model
              )

set_tracing_disabled(disabled=True)


def main():
    result = Runner.run_sync(
        agent, "tell about living in Australia or England as of current immigration, work, study and lifestyle situation", run_config=config)
    print(result.final_output)


if __name__ == "__main__":
    main()
