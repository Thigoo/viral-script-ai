from agents.creative_agent import CreativeAgent
from agents.critic_agent import CriticAgent
from agents.refinement_agent import RefinementAgent
from utils.helper import estimate_duration_from_text
from config import CREATIVE_AI_MODEL, CRITIC_AI_MODEL, REFINEMENT_AI_MODEL, client

IDEAL_MIN_DURATION = 50
IDEAL_MAX_DURATION = 60
# MIN_SCORE = 7
# MAX_ITERATIONS = 1


def run_pipeline(theme: str) -> dict:

    creative = CreativeAgent(
        client=client,
        ai_model=CREATIVE_AI_MODEL,
        temperature=0.7
        )
    critic_agent = CriticAgent(
        client=client,
        ai_model=CRITIC_AI_MODEL,
        temperature=0.3
        )
    refiner = RefinementAgent(
        client=client,
        ai_model=REFINEMENT_AI_MODEL,
        temperature=0.5
        )

    initial_script = creative.generate_script(theme)

    initial_duration = estimate_duration_from_text(initial_script)

    initial_critic = critic_agent.evaluate(theme, initial_script)

    final_script = refiner.refine(
        theme, 
        initial_script, 
        initial_critic,
        current_duration=initial_duration,
        target_min_duration=IDEAL_MIN_DURATION,
        target_max_duration=IDEAL_MAX_DURATION
    )

    final_duration = estimate_duration_from_text(final_script)

    return {
        "initial_script": initial_script,
        "initial_duration": initial_duration,
        "initial_critic": initial_critic,
        "final_script": final_script,
        "final_duration": final_duration,
    }
