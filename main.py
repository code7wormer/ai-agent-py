import os
from dotenv import load_dotenv
load_dotenv()
ai_key=os.getenv("OPENROUTER_API_KEY")


def main():
    print("Hello from agent-py!")


if __name__ == "__main__":
    main()
