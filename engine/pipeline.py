from agents.creative_agent import CreativeAgent
from agents.critic_agent import CriticAgent
from agents.refinement_agent import RefinementAgent
from utils.helper import estimate_duration_from_text
from config import CREATIVE_AI_MODEL, CRITIC_AI_MODEL, REFINEMENT_AI_MODEL, client

IDEAL_MIN_DURATION = 55
IDEAL_MAX_DURATION = 65
MIN_SCORE = 7
MAX_ITERATIONS = 3


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

    current_script = creative.generate_script(theme)

    initial_script = current_script 

    iterations_data = []

    iteration = 0

    while iteration < MAX_ITERATIONS:

        real_duration = estimate_duration_from_text(current_script)

        critic_result = critic_agent.evaluate(theme, current_script)

        critic_data = critic_result

        duration_ok = IDEAL_MIN_DURATION <= real_duration <= IDEAL_MAX_DURATION

        quality_ok = (
            critic_data["hook_score"] >= MIN_SCORE and
            critic_data["retention_score"] >= MIN_SCORE and
            critic_data["depth_score"] >= MIN_SCORE
        )

        critic_flag = critic_data["needs_refinement"]

        iterations_data.append({
            "iteration": iteration + 1,
            "duration": real_duration,
            "critic": critic_result
        })

        if duration_ok and quality_ok and not critic_flag:
            break

        current_script = refiner.refine(
            theme=theme,
            script=current_script,
            critic=critic_data
        )

        iteration += 1

    final_duration = estimate_duration_from_text(current_script)

    return {
        "initial_script": initial_script,
        "iterations": iterations_data,
        "final_script": current_script,
        "final_duration": final_duration
    }