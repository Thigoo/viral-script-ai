from agents.creative_agent import generate_script
from agents.critic_agent import generate_critic
from agents.refinement_agent import generate_refinement
from utils.helper import estimate_duration_from_text

IDEAL_MIN_DURATION = 55
IDEAL_MAX_DURATION = 65
MIN_SCORE = 7
MAX_ITERATIONS = 3

def run_pipeline(theme: str) -> dict:

    current_script = generate_script(theme)

    iterations_data = []

    iteration = 0

    while iteration < MAX_ITERATIONS:

        real_duration = estimate_duration_from_text(current_script)
        critic = generate_critic(theme, current_script)

        duration_ok = IDEAL_MIN_DURATION <= real_duration <= IDEAL_MAX_DURATION

        quality_ok = (
            critic['critica']['hook_score'] >= MIN_SCORE and
            critic['critica']['retention_score'] >= MIN_SCORE and
            critic['critica']['depth_score'] >= MIN_SCORE
        )

        critic_flag = critic['critica']['needs_refinement']

        iterations_data.append({
            "iteration": iteration + 1,
            "duration": real_duration,
            "critic": critic
        })

        if duration_ok and quality_ok and not critic_flag:
            break

        current_script = generate_refinement(
            theme=theme,
            script=current_script,
            critic=critic['critica']
        )

        iteration += 1

    final_duration = estimate_duration_from_text(current_script)

    return {
        "initial_script": current_script if iteration == 0 else None,
        "iterations": iterations_data,
        "final_script": current_script,
        "final_duration": final_duration
    }