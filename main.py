from agents.creative_agent import generate_script
from agents.critic_agent import generate_critic
from agents.refinement_agent import generate_refinement
from utils.helper import estimate_duration_from_text
import json

if __name__ == '__main__':
    theme = 'Ainda vale a pena dropshipping em 2026?'

    current_script = generate_script(theme)

    print('\n=== SCRIPT INICIAL ===\n')
    print(current_script)

    IDEAL_MIN_DURATION = 55
    IDEAL_MAX_DURATION = 65

    MIN_SCORE = 7

    MAX_ITERATIONS = 3
    iteration = 0

    while iteration < MAX_ITERATIONS:

        real_duration = estimate_duration_from_text(current_script)
        critic = generate_critic(theme, current_script)

        print(f'\n=== ITERAÇÃO {iteration + 1} ===')
        print(f'REAL DURATION ->> {real_duration}s')
        print(json.dumps(critic, indent=4, ensure_ascii=False))

        duration_ok = IDEAL_MIN_DURATION <= real_duration <= IDEAL_MAX_DURATION

        quality_ok = (
            critic['critica']['hook_score'] >= MIN_SCORE and
            critic['critica']['retention_score'] >= MIN_SCORE and
            critic['critica']['depth_score'] >= MIN_SCORE
        )

        critic_flag = critic['critica']['needs_refinement']

        if duration_ok and quality_ok and not critic_flag:
            print('\n=== CRITÉRIOS ATINGIDOS ===\n')
            break

        print('\n=== REFINANDO... ===\n')

        refinement_data = {
            'theme': theme,
            'script': current_script,
            'critic': critic['critica'],
        }

        current_script = generate_refinement(**refinement_data)

        iteration += 1

    final_script = current_script

    print('\n=== SCRIPT FINAL ===\n')
    print(final_script)

    final_duration = estimate_duration_from_text(final_script)
    print(f'\nFINAL DURATION ->> {final_duration}s')