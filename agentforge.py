from agents import Agent

from tools import (
    analyze_user_goal,
    generate_agent_blueprint,
    evaluate_agent_architecture,
    optimize_agent_prompt,
    create_documentation
)

from pathlib import Path

PROMPT_FILE = Path(__file__).parent / "prompt" / "agentforge_instructions.txt"

with open(PROMPT_FILE, "r", encoding="utf-8") as file:
    instructions = file.read()

AgentForge = Agent(
    name="AgentForge",
    instructions=instructions,
    tools=[
        analyze_user_goal,
        generate_agent_blueprint,
        evaluate_agent_architecture,
        optimize_agent_prompt,
        create_documentation
    ]
)

