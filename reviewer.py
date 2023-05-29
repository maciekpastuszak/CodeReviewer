import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

PROMPT = """
You will receive a file's contents as text.
Generate a code review for the file. Indicate what changes should be made to improve its style, performance, readibility and maintainability. If there are any reputable libraries that could be introduced to improve the code, suggest them. Be kind and constructive. For each suggested change, include line numbers to which you are referring.
"""

filecontent = """
def mystery(x,y):
retunr x ** y
"""


def code_review(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    generated_code_review = make_code_review_req(content, model)
    print(generated_code_review)


def make_code_review_req(filecontent, model):
    messages = [
        {"role": "system", "content": PROMPT},
        {"role": "user", "content": f"Code review the following file: {filecontent}"},
    ]

    res = openai.ChatCompletion.create(model=model, messages=messages)

    return res["choices"][0]["message"]


code_review("tree.py", "gpt-3.5-turbo")
