class BaseAgent:
    def __init__(self, client, ai_model, temperature):
        self.client = client
        self.ai_model = ai_model
        self.temperature = temperature

    def call_llm(self, messages):
        response = self.client.chat.completions.create(
            model=self.ai_model,
            messages=messages,
            temperature=self.temperature
        )

        return response.choices[0].message.content