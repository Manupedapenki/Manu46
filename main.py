import sys
import os

# Add project root to path
sys.path.append(os.path.abspath("."))

# Import provider factory
from utils.llm_service import LLMFactory


def main():

    print("🤖 Multi Provider Chatbot Started")
    print("Type 'exit' to stop\n")

    # Create Gemini provider
    provider = LLMFactory.get_provider("gemini")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chatbot stopped")
            break

        response = provider.generate(user_input)

        print("\nAI:", response)
        print()


if __name__ == "__main__":
    main()
