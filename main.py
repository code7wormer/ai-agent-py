import os
from dotenv import load_dotenv
from openai import OpenAI
from openai.resources.admin.organization import usage
import argparse

import json
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file

from callables import available_functions, call_function
from prompt import system_prompt
from test_get_file_content import result

load_dotenv()
api_key=os.getenv("OPENROUTER_API_KEY",default=None)
if api_key is None:
    raise RuntimeError("Couldn't fetch OpenRouter key")



client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)
parser=argparse.ArgumentParser(description="agent-openrouter")
parser.add_argument("prompt",type=str,help="User Prompt")
parser.add_argument("--verbose",action="store_true",help="Detailed info")
arg=parser.parse_args()


messages=[
    {"role":"system","content":system_prompt},
    {"role":"user","content" :arg.prompt }
]

def main():
    for _ in range(20):
        response=client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_functions,
        )

        message = response.choices[0].message
        messages.append(message)

        if not message.tool_calls:
            print(message.content)
            break

        for call in message.tool_calls:
            output_message=call_function(call, arg.verbose)

            messages.append(output_message)
            if not output_message["content"]:
                raise Exception( "Function returned no content")
            if arg.verbose:
                print(f"-> {output_message['content']}")
    else:
        print("Agent reached maximum iterations without finishing.")
        exit(1)

if __name__ == "__main__":
    main()
