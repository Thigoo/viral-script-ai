from agents.base_agent import BaseAgent
from prompts import REFINEMENT_SYSTEM_PROMPT, REFINEMENT_USER_PROMPT

class RefinementAgent(BaseAgent):
    def refine(self, theme: str, script: str, critic: dict) -> str:
        user_prompt = REFINEMENT_USER_PROMPT.format(
            theme=theme,
            script=script,
            hook_score=critic["hook_score"],
            retention_score=critic["retention_score"],
            depth_score=critic["depth_score"],
            clarity_score=critic["clarity_score"],
            theme_alignment_score=critic["theme_alignment_score"],
            feedback=critic["feedback"]
        )

        messages = [
            {'role': 'system', 'content': REFINEMENT_SYSTEM_PROMPT},
            {'role': 'user', 'content': user_prompt},
        ]

        return self.call_llm(messages)
