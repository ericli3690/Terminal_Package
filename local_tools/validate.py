"""VALIDATE.PY VERSION 3.2
Validates user input and handles errors
Includes:
- log_error(reason): print an error statement to the console with the provided reason.
- ask(prompt:str, conditions:list, errors:list, variables:dict): asks the user a question 'prompt', checking it against every element in the list 'conditions', printing the corresponding element in the list 'errors' on a condition failure and asking the user to input an answer again; variables used in 'conditions' can be given to the ask() function via the dictionary 'variables' and used in 'conditions' using the syntax var['variable_name_here']
"""

### imports
import re
# printer for colour printing strings
from local_tools.printer import colour_print

def log_error(reason="Please re-input."):
    """Prints an error message in red, including reason"""
    colour_print("Denied. " + reason, 'red')

def ask(prompt:str, conditions:list, errors:list, variables:dict={}, disallow_null:bool=True):
  """Repeatedly asks the user a question until their answer is deemed appropriate, fulfilling all elements of list 'conditions', at which point it exits and returns the user's answer; On failure, it will print an error message corresponding with the condition failed.
  - prompt may be a string or an f-string
  - conditions must be a list with string elements, and any variables called must be formatted as var['variable_name_here'] (note the quotes)
  - variables must be a dictionary with string keys and variable values; the key must be identical to the variable namespace except for type
  - errors must be a list with string or f-string elements
  - note that a common inputting error is where the lists required are formatted as ['a, b'] and not ['a', 'b']"""
  while True:
    # ask the user 'prompt'
    restart = False
    answer = input(prompt)

    var = variables

    if disallow_null:
      conditions.insert(0, "answer != ''")
      errors.insert(0, "Please input a value.")
    
    # for every condition that was passed in, check if the answer fulfills it
    # if a condition is not fulfilled, log the condition that caused it, restart the loop, and ask for the condition again
    for condition in conditions:
      if not eval(condition):
        index_of_condition_failed = conditions.index(condition)
        colour_print("Denied. " + errors[index_of_condition_failed], 'red')
        restart = True
        break
    if restart:
      continue

    # if all conditions evaluated to true, print a success message and return the answer
    colour_print('Accepted.', 'green')
    return answer