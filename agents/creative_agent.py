from config import client, CREATIVE_AI_MODEL
from prompts import CREATIVE_SYSTEM_PROMPT

def generate_script(theme: str) -> str:
    if not theme.strip():
        return 'Tema inválido.'
    
    system_prompt = CREATIVE_SYSTEM_PROMPT
    user_prompt = f'Content theme: {theme}'
    try:
        response = client.chat.completions.create(
        model = CREATIVE_AI_MODEL,
        messages = [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt}
        ],
        temperature=0.8
    )
        return response.choices[0].message.content
    
    except Exception as e:
        print(f'Erro ao gerar roteiro: {e}')
        return 'Ocorreu um erro ao gerar o roteiro.'
