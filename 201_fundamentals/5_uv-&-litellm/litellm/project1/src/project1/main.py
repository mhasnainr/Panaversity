from litellm import completion
import os

## set ENV variables
os.environ["GEMINI_API_KEY"] = "your-api-key"

def call_gemini():
    response = completion(
        model="google/gemini-2.5-flash",
        messages=[{ "content": "Hello, how are you?","role": "user"}]
    )
    print(response)

    # print(response['choices'][0]['message']['content'])