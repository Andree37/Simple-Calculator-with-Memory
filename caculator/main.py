# -*- coding: utf-8 -*-
"""
Created on Mon Oct 08 14:18:03 2020
Python calculator
@author: andre
"""
import re


class Calculator:
    def __init__(self):
        self.memory = []
        self.regex = r'(\d+\s*(\*|\/|\+|\-)\s*)+(\d+\s*)'

    def _evaluate(self, expression):
        try:
            result = eval(expression)
            self.memory.append({expression, result})
            return result
        except ZeroDivisionError as err:
            print("You can not divide by 0")

    def _process_calculation(self, expression):
        regex = re.compile(self.regex)
        result = regex.match(expression)

        if not result:
            raise ValueError
        # return result to be calculated, with only the math part in it
        return self._evaluate(result.group(0))

    def calculate(self, expression):
        try:
            return self._process_calculation(expression)
        except ValueError as err:
            print(err)
            return "Please include a simple math expression with no parentheses"


if __name__ == '__main__':
    calculator = Calculator()
    print("Hello user this is a calculator:")
    print("Be sure to write expressions as correctly as possible, just as follows:")
    print("1 + 2, 2 * 1 * 4, etc")
    print("{first_param} {operation} {second_param}, where we can have many params but no '()' ")
    print("For this example we only utilize integers. Floats and Booleans will return as an error")
    print("Write 'quit' to exit the application")
    while True:
        expression = input("Simple expression >")
        if "quit" in expression.lower():
            break
        result = calculator.calculate(expression)
        print(f"Result : {result}")
        print(f"Past Results: {calculator.memory}")
