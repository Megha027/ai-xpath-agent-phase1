import ollama
from utils.prompt_loader import load_prompt
from utils.response_parser import ResponseParser


class AIAgent:

    def __init__(self, model="qwen2.5:3b"):
        self.model = model

    def generate_xpath(self, element):

        prompt = load_prompt("xpath_prompt.txt")

        prompt = prompt.format(
            html=element.html
        )

        # Call Ollama
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        print("\n========== RAW AI RESPONSE ==========")
        print(response["message"]["content"])
        print("=====================================")

        xpath = ResponseParser.extract_xpath(
            response["message"]["content"]
        )

        print("Parsed XPath :", xpath)

        return xpath