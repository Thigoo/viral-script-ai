from config import client, AI_MODEL
from prompts import SYSTEM_PROMPT

def generate_script(theme: str) -> str:
    if not theme.strip():
        return 'Tema inválido.'
    
    system_prompt = SYSTEM_PROMPT
    user_prompt = f'Tema do vídeo: {theme}'

    try:
        response = client.chat.completions.create(
        model = AI_MODEL,
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
