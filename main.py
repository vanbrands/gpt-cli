import openai
import warnings

from rich import print
from rich.markdown import Markdown
from termcolor import colored

warnings.filterwarnings("ignore")

def get_openai_response(prompt):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        temperature=0.7,
    )

    return Markdown(response.choices[0]['message']['content'])

def main():

    while True:

        prompt = input(colored("You: ", "green"))
        
        if prompt.lower() in ["exit", "quit"]:
            break
        response = get_openai_response(prompt)

        print('\n')
        print(response)
        print('\n')

if __name__ == "__main__":
    main()