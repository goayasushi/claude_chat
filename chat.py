import anthropic
import os
from dotenv import load_dotenv
from memory_profiler import profile

# load .env
load_dotenv()

# Claude api key
API_KEY = os.getenv("CLAUDE_API_KEY")

client = anthropic.Anthropic(
    api_key=API_KEY,
)


# verify memory consumption
@profile
def call_claude_api(question):
    # message create: https://docs.anthropic.com/en/docs/initial-setup
    message = client.messages.create(
        # claude model: https://docs.anthropic.com/en/docs/about-claude/models
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        temperature=0.7,
        messages=[{"role": "user", "content": question}],
    )

    # extract answer from response
    answer = "".join([block.text for block in message.content])
    print(f"\nClaude: {answer}\n")
    return answer


if __name__ == "__main__":
    while True:
        question = input("your question: ")
        # exit or quit to end chat
        if question.lower() in ["exit", "quit"]:
            print("Exiting...")
            break
        call_claude_api(question)
