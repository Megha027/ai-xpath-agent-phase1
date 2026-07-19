from pathlib import Path


def load_prompt(filename):

    project_root = Path(__file__).resolve().parent.parent

    prompt_file = project_root / "prompts" / filename

    with open(prompt_file, "r", encoding="utf-8") as file:
        return file.read()