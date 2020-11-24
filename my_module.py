"""
My Module
"""

import json

breakpoint()

def greeting():
    return"Hello Bridget"

breakpoint()

def letter_text(**kwargs):
    if "name" and "amount" and "denomination" in kwargs.keys():
        return"Hello {kwargs['Bridget']}, this letter is to inform you that \
            you have won {kwargs['amount']} {kwargs['denomination']},"
    return"incorrect parameters supplied"

breakpoint()

my_json_data = {}

with open("input.json", "r") as input:
    my_json_data = json.load(input)

breakpoint()
