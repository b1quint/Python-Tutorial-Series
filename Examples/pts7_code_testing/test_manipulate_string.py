#!/usr/bin/env python
"""
Tests for manipulate_strings.py
"""

import manipulate_strings
import pytest


def test_capital_case():
    assert manipulate_strings.capital_case('semaphore') == 'Semaphore'


def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        manipulate_strings.capital_case(9)


if __name__ == '__main__':
    pytest.main()
