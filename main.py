import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import SYSTEM_PROMPT
from call_functions import available_functions, call_function

def main():
    load_dotenv()

    verbose_flag = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    user_prompt = " ".join(args)

    if verbose_flag:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    loop_counter = 0
    done = False

    while not done and loop_counter < 20:
        done = generate_content(client, messages, verbose_flag)
        loop_counter += 1

    # generate_content(client, messages, verbose_flag)

def generate_content(client, messages, verbose_flag):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=SYSTEM_PROMPT)
    )
    if verbose_flag:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
        
    # print("Response:")
    if response.function_calls is not None and len(response.function_calls) > 0:
        for function_call in response.function_calls:
            # print(f"Calling function: {function_call.name}({function_call.args})")
            function_call_result = call_function(function_call, verbose_flag)
            if "result" not in function_call_result.parts[0].function_response.response:
                raise Exception("SOMETHING FATAL HAPPENED")
            
            if verbose_flag:
                print(f"-> {function_call_result.parts[0].function_response.response}")
            
            for candidate in response.candidates:
                messages.append(candidate.content)

            messages.append(function_call_result)

    else:
        print(response.text)
        return True

if __name__ == "__main__":
    main()