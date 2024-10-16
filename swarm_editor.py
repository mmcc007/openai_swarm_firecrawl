from swarm import Swarm, Agent
from swarm.core import Result
import json
from typing import Dict, List

class SwarmEditor:
    def __init__(self):
        self.agents: List[Agent] = []
        self.swarm = Swarm()

    def add_agent(self, name: str, instructions: str):
        self.agents.append(Agent(
            name=name,
            instructions=instructions
        ))

    def update_agent(self, index: int, name: str, instructions: str):
        if 0 <= index < len(self.agents):
            self.agents[index] = Agent(
                name=name,
                instructions=instructions
            )

    def load_configuration(self, config_file: str):
        with open(config_file, 'r') as f:
            config = json.load(f)
        
        self.agents = []
        for agent_config in config['agents']:
            self.add_agent(agent_config['name'], agent_config['instructions'])

    def run_workflow(self, initial_input: str):
        response = None
        context_variables = {}
        for agent in self.agents:
            response = self.swarm.run(
                agent=agent,
                messages=[{"role": "user", "content": initial_input}] if response is None else response.messages,
                context_variables=context_variables,
                max_turns=1
            )
            context_variables.update(response.context_variables)
            initial_input = response.messages[-1]["content"]
        return response
    
    def run_single_agent(self, agent, initial_input):
        response = self.swarm.run(
            agent=agent,
            messages=[{"role": "user", "content": initial_input}],
            context_variables={},
            max_turns=1
        )
        return response