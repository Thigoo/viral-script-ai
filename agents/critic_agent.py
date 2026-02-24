from prompts import CRITIC_SYSTEM_PROMPT
from config import client, CRITIC_AI_MODEL
import json

def generate_critic(theme: str, script: str) -> dict:
    if not theme or not script:
        return f'Tema ou roteiro faltantes para a crítica'
        
    user_prompt = f'Content theme: {theme}\n Created script: {script}'

    try:
        response = client.chat.completions.create(
            model=CRITIC_AI_MODEL,
            messages=[
                {'role': 'system', 'content': CRITIC_SYSTEM_PROMPT},
                {'role': 'user', 'content': user_prompt}
            ],
            temperature=0.3
        )

        data = response.choices[0].message.content
        parsed_data = json.loads(data)

        return {'critica': parsed_data}
    
    except Exception as e:
        print(f'Erro ao criar crítica: {e}')
        return 'Não foi possível fazer a crítica'