import os

from groq import Groq

from app.utils.logger import generator_logger


class LlamaContentGenerator:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = "llama3-8b-8192"  # or use another Groq-supported model

    def generate_content(self, prompt: str) -> str:
        generator_logger.info(
            f"generator - Generating content with LLaMA via Groq: prompt: {prompt}"  # noqa
        )

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant that crafts personalized messages.",  # noqa
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.7,
                max_tokens=500,
            )
            content = response.choices[0].message.content.strip()
            generator_logger.info(f"LLaMA via Groq response: {content}")
            return content
        except Exception as e:
            generator_logger.error(f"LLaMA (Groq) generation failed: {str(e)}")
            return "LLaMA (Groq) generation error."
