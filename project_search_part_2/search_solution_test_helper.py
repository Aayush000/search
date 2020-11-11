import io
from search_tests_helper import get_print
from unittest import TestCase, main
from unittest.mock import patch
import sys

@patch('builtins.input')
def test_all(answers, input_mock):
    print(get_print(input_mock, answers))

if __name__ == '__main__':
    keyword = input()
    option = int(input())
    if option != 5 and option != 7:
        resp = int(input()) if option < 4 else input()
        test_all([keyword, option, resp])
    else:
        test_all([keyword, option])
