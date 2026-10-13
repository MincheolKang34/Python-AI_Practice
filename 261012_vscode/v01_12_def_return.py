import pyfiglet
from termcolor import colored

def make_highlight(text:str):
    pyfiglet.figlet_format(text)
    """
    입력된 문자열을  pyfiglet, termcolor를 이용하여 꾸며준다.

    Args:
        text (str): 꾸며줄 문자열
    """
    py_text = pyfiglet.figlet_format(text)
    color_py_text = colored(py_text, 'red')
    return color_py_text

# highlighted_text = make_highlight("Hello")
# print(highlighted_text)
print(make_highlight("Hello"))