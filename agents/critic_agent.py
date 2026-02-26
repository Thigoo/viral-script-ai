from agents.base_agent import BaseAgent
from prompts import CRITIC_SYSTEM_PROMPT
import json

class CriticAgent(BaseAgent):
    def evaluate(self, theme: str, script: str) -> dict:
        messages = [
            {'role': 'system', 'content': CRITIC_SYSTEM_PROMPT},
            {'role': 'user', 'content': f"Theme: {theme}\n\nScript:\n{script}"}
        ]

        response = self.call_llm(messages)

        return json.loads(response)