from prompts import CREATIVE_SYSTEM_PROMPT
from agents.base_agent import BaseAgent

class CreativeAgent(BaseAgent):
    def generate_script(self, theme: str) -> str:
        messages = [
            {'role': 'system', 'content': CREATIVE_SYSTEM_PROMPT},
            {'role': 'user', 'content': theme}
        ]

        return self.call_llm(messages)