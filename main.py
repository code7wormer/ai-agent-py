import os
from dotenv import load_dotenv
from openai import OpenAI
from openai.resources.admin.organization import usage
import argparse

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

messages=[{"role":"user","content" :arg.prompt }]
response=client.chat.completions.create(model="openrouter/free",messages=messages)




def main():
    if arg.verbose:
        print("User prompt:",arg.prompt)
        print(response.choices[0].message.content)
        print("Prompt tokens:",response.usage.prompt_tokens)
        print("Response tokens:",response.usage.completion_tokens )
    else:
        print(response.choices[0].message.content)
if __name__ == "__main__":
    main()
