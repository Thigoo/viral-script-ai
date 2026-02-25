from agents.creative_agent import generate_script
from agents.critic_agent import generate_critic
from agents.refinement_agent import generate_refinement
import json

if __name__ == '__main__':
    theme = 'Por que o pão de acúcar tem esse nome?'

    script = generate_script(theme)
    print('\n=== ROTEIRO GERADO ===\n')
    print(script)

    critic = generate_critic(theme, script)
    print('\n=== CRÍTICA GERADA ===\n')
    print(json.dumps(critic, indent=4, ensure_ascii=False))

    force_refinement = False

    if critic['critica']['estimated_duration_seconds'] < 45:
        force_refinement = True

    needs_refinement = critic['critica']['needs_refinement'] or force_refinement

    if not needs_refinement:
        print('\n=== NÃO REQUER REFINAMENTO ===\n')
        final_script = script
    else:
        refinement_data = {
            'theme': theme,
            'script': script,
            'critic': critic['critica'],
        }
        final_script = generate_refinement(**refinement_data)

    print('\n=== SCRIPT FINAL ===\n')
    print(final_script)
