import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv('AI_API_KEY')
BASE_URL = 'https://openrouter.ai/api/v1'
CREATIVE_AI_MODEL = 'arcee-ai/trinity-large-preview:free'
CRITIC_AI_MODEL = 'liquid/lfm-2.5-1.2b-thinking:free'

client = OpenAI(
    api_key = API_KEY,
    base_url = BASE_URL
)