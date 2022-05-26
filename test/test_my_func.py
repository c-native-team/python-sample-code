from os.path import dirname, abspath
import sys

parent_dir = dirname(dirname(abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from src.my_func import input_string

def test_print():
    res = input_string("Hello World")
    assert res == "Hello World"
