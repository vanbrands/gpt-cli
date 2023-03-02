import openai
import warnings

from rich import print
from rich.markdown import Markdown
from termcolor import colored

warnings.filterwarnings("ignore")

def get_openai_response(messages):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
    )

    return response.choices[0]['message']

def main():

    messages = []

    while True:

        prompt = input(colored("You: ", "green"))
        
        if prompt.lower() in ["exit", "quit"]:
            break

        messages.append({"role": "user", "content": prompt})
        
        response = get_openai_response(messages)
        messages.append(dict(response))

        print('\n')
        print(Markdown(response['content']))
        print('\n')

if __name__ == "__main__":
    main()it