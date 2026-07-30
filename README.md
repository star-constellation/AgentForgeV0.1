# AgentForge V0.1

An AI Agent Architect that transforms ideas into structured AI agent systems.

AgentForge helps design AI agents by analyzing:
* Purpose
* Required capabilities
* Tools
* Limitations
* Evaluation methods

## Features

Current V0.1 features:

* User goal analysis
* Basic agent blueprint generation
* Architecture evaluation
* Prompt optimization
* Documentation generation

## Project Structure
AgentForgeV0.1/
│
├── main.py
├── agentforge.py
├── tools.py
├── prompts/
│ └── agentforge_instructions.txt
├── .env.example
├── requirements.txt
└── README.md


## Installation
Clone the repository:
git clone <repository-url>
cd AgentForgeV0.1

## Create virtual environment
python -m venv .venv
Linux:
source .venv/bin/activate
# Install dependencies:
pip install -r requirements.txt

## Environment Setup
#Create a .env file:
cp .env.example .env
Add your API key:
OPENAI_API_KEY=your_api_key_here

## Usage
Run AgentForge:
python main.py

# Example:
=^ AgentForge V0.1 ^=

What agent do you want to create?
> Create a Linux ricing assistant

##Current Limitations
V0.1 is an early prototype.

#Limitations:
* Tools are currently simple implementations
* No long-term memory system
* No multi-agent collaboration
* Limited evaluation capabilities
* No production deployment system


