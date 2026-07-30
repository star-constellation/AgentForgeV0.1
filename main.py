from dotenv import load_dotenv

load_dotenv()

from agents import Runner
from agentforge import AgentForge

def main():
    print("=^ AgentForge V0.1 ^=")

    user_input = input(
          "\nWhat agent do you want to create?\n> "
)

    result = Runner.run_sync(
        AgentForge,
        user_input
    )

    print("\n=== AgentForge Output ===")
    print(result.final_output)


if __name__ == "__main__":
    main()
