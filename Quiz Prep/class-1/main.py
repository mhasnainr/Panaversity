import os
from agents import Agent, Runner, set_tracing_disabled
from agents.run import RunConfig
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, set_default_openai_api
from dotenv import load_dotenv

load_dotenv()


GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set.")

set_default_openai_api("chat_completions")

external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

set_default_openai_api(external_client)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,

)


agent = Agent(name="Assistant",
              instructions="You are a helpful assistant",
              model=model
              )

set_tracing_disabled(disabled=True)
# constructor call has 2 parameters (name, instructions [system prompt])


def main():
    result = Runner.run_sync(
        agent, "tell about Meta's poachment of OpenAI's employees", run_config=config)
    print(result.final_output)


if __name__ == "__main__":
    main()
