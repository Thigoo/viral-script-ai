from config import client, REFINEMENT_AI_MODEL
from prompts import REFINEMENT_SYSTEM_PROMPT

def generate_refinement(**data) -> str:
    user_prompt = f"""Content theme: {data["theme"]}

Original script:
{data["script"]}

Critic scores:
Hook: {data['critic']["hook_score"]}
Retention: {data['critic']["retention_score"]}
Depth: {data['critic']["depth_score"]}
Clarity: {data['critic']["clarity_score"]}
Theme alignment: {data['critic']["theme_alignment_score"]}

Feedback:
{data['critic']["feedback"]}
    """

    try:
        response = client.chat.completions.create(
            model=REFINEMENT_AI_MODEL,
            messages=[
                {'role': 'system', 'content': REFINEMENT_SYSTEM_PROMPT},
                {'role': 'user', 'content': user_prompt}
            ],
            temperature=0.5
        )

        return response.choices[0].message.content
    
    except Exception as e:
        print(f'Erro ao criar refinamento: {e}')
        return 'Ocorreu um erro ao gerar o refinamento.'
