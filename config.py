import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv('AI_API_KEY')
BASE_URL = 'https://openrouter.ai/api/v1'
AI_MODEL = 'arcee-ai/trinity-large-preview:free'

client = OpenAI(
    api_key = API_KEY,
    base_url = BASE_URL
)