import openai

from app.content_generator.base import ContentGenerator
from app.settings import OPEN_AI_MODEL_PROVIDER, OPENAI_API_KEY
from app.utils.logger import generator_logger


class OpenAIContentGenerator(ContentGenerator):
    """
    Content generator using OpenAI's GPT-4 model.
    """

    def __init__(self):
        self.api_key = OPENAI_API_KEY
        self.client = self._initialize_client()

    def _initialize_client(self):
        """
        Initialize the OpenAI client with the provided API key.
        """
        openai.api_key = self.api_key
        return openai

    def generate_content(self, prompt: str) -> str:
        generator_logger.info(f"Generating content prompt: {prompt}")
        try:
            response = self.client.chat.completions.create(
                model=OPEN_AI_MODEL_PROVIDER,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a skilled content creator.",
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.9,
                max_tokens=800,  # Higher limit to allow multiple suggestions
            )
            content = response.choices[0].message.content.strip()

            generator_logger.info("OpenAI response:\n%s", content)
            return content
        except Exception as e:
            generator_logger.error(f"Error generating content: {e}")
            return "Error generating content. Please try again."
