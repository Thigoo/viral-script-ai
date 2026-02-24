from agents.creative_agent import generate_script
from agents.critic_agent import generate_critic
import json

if __name__ == '__main__':
    theme = 'Por que o pão de acúcar tem esse nome?'
    script = generate_script(theme)
    response = generate_critic(theme, script)
    # print('\n=== ROTEIRO GERADO ===\n')
    # print(script)
    print('\n=== CRÍTICA GERADA ===\n')
    print(json.dumps(response, indent=4, ensure_ascii=False))
