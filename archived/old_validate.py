"""VALIDATE.PY
Validates user input and handles errors
Includes:
- log_error(reason): print an error statement to the console with the provided reason.
- validate(to_check, required_type): check if the parameter to_check is of the same type as required_type, returning to_check if they are identical or False if they are not
- ask_question_validate(prompt, type_of_answer): repeatedly asks the user for an input of parameter prompt until it gets one matching type_of_answer; it does this checking through validate()
- ask_question_eval_vague(prompt, conditions): like the above but does not rely on validate, instead allowing the programmer to input the code to run when it is called, evaling it
- ask_question_eval_explicit(prompt, conditions): like the above but uses a list of conditions, allowing it to log exactly which condition was unfulfilled instead of a general error message
- ask_question_eval_explicit_friendly(prompt, conditions, errors): like the above but adds a list of errors, allowing it to long which condition was unfulfilled in a human manner
- ask(prompt:str, conditions:list, variables:dict, errors:list): asks the user a question 'prompt', checking it against every element in the list 'conditions', printing the corresponding element in the list 'errors' on a condition failure and asking the user to input an answer again; variables used in 'conditions' can be given to the ask() function via the dictionary 'variables' and used in 'conditions' using the syntax var['variable_name_here']
"""

# imports
# colour_printer for colour printing strings
import re
from colour_printer import colour_print

def log_error(reason="Please re-input."):
    """log_error(reason)
    Prints an error message in red, including reason"""
    colour_print("Denied. This is not a valid value: " + reason, 'red')

def validate(to_check, required_type):
  """validate(to_check, required_type)
  Checks if to_check matches multiple types, returning to_check if it does and False if it doesn't
  Otherwise, it prints an error to the console using log_error
  These types include:
  - int: all characters in the string are a number
  - yn: either the character y or n
  - str: the type of to_check is a string"""
  if required_type == 'int' and all(char.isdigit() for char in to_check):
    # if every character isdigit
    return to_check
  elif required_type == 'yn' and (to_check == 'y' or to_check == 'n'):
    # if either the character y or n
    return to_check
  elif required_type == 'str' and type(to_check) == str:
    # if its just a string
    return to_check
  else:
    log_error()
    return False

def ask_question_validate(prompt: str, type_of_answer: str):
  """ask_question_validate(prompt, type_of_answer)
  Repeatedly asks the user a question until their answer, through validate(), is deemed appropriate, at which point it exits and returns the user's answer"""
  while True:
    # ask the user (prompt)
    answer = input(prompt)
    # if validate gives a truthy reply, print accepted and return what the user typed
    # if it is an invalid answer, validate prints its error statement and returns False, making the infinite loop continue
    if validate(answer, type_of_answer):
      colour_print('Accepted.', 'green')
      return answer

def ask_question_eval_vague(prompt: str, conditions: str):
  """ask_question_eval_vague(prompt, type_of_answer)
  Repeatedly asks the user a question until their answer is deemed appropriate, fulfilling evaluation of hte string 'conditions', at which point it exits and returns the user's answer; On failure, the mistake made by the user will not be outputted."""
  while True:
    # ask the user (prompt)
    answer = input(prompt)
    # if the user's answer fulfills the conditions (eval on a string to turn it into code), return answer, else repeat
    # note: eval is actually a risky, nonstandard bit of code due to its security implications (turning any string into runnable code) but in this context it should be safe
    if eval(conditions):
      colour_print('Accepted.', 'green')
      return answer
    else:
      colour_print("Denied. This is not a valid value.", 'red')

def ask_question_eval_explicit(prompt: str, conditions: list):
  """ask_question_eval_explicit(prompt, type_of_answer)
  Repeatedly asks the user a question until their answer is deemed appropriate, fulfilling all elements of list 'conditions', at which point it exits and returns the user's answer; On failure, it will print the exact condition that caused the failure."""
  while True:
    # ask the user 'prompt'
    restart = False
    answer = input(prompt)
    
    # for every condition that was passed in, check if the answer fulfills it
    # if a condition is not fulfilled, log the condition that caused it, restart the loop, and ask for the condition again
    for condition in conditions:
      if not eval(condition):
        colour_print("Denied. Condition not fulfilled: " + condition, 'red')
        restart = True
        break
    if restart:
      continue

    # if all conditions evaluated to true, print a success message and return the answer
    colour_print('Accepted.', 'green')
    return answer

def ask_question_eval_explicit_friendly(prompt: str, conditions: list, errors: list):
  """ask_question_eval_explicit(prompt, type_of_answer)
  Repeatedly asks the user a question until their answer is deemed appropriate, fulfilling all elements of list 'conditions', at which point it exits and returns the user's answer; On failure, it will print the exact condition that caused the failure."""
  while True:
    # ask the user 'prompt'
    restart = False
    answer = input(prompt)
    
    # for every condition that was passed in, check if the answer fulfills it
    # if a condition is not fulfilled, log the condition that caused it, restart the loop, and ask for the condition again
    for condition in conditions:
      if not eval(condition):
        index_of_condition_failed = conditions.index(condition)
        colour_print("Denied. Condition not fulfilled: " + errors[index_of_condition_failed], 'red')
        restart = True
        break
    if restart:
      continue

    # if all conditions evaluated to true, print a success message and return the answer
    colour_print('Accepted.', 'green')
    return answer

def ask(prompt:str, conditions:list, variables:dict, errors:list):
  """ask_question_eval_explicit(prompt:str, conditions:list, variables:dict, errors:list)
  Repeatedly asks the user a question until their answer is deemed appropriate, fulfilling all elements of list 'conditions', at which point it exits and returns the user's answer; On failure, it will print an error message corresponding with the condition failed.
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
    
    # for every condition that was passed in, check if the answer fulfills it
    # if a condition is not fulfilled, log the condition that caused it, restart the loop, and ask for the condition again
    for condition in conditions:
      if not eval(condition):
        index_of_condition_failed = conditions.index(condition)
        colour_print("Denied. Condition not fulfilled: " + errors[index_of_condition_failed], 'red')
        restart = True
        break
    if restart:
      continue

    # if all conditions evaluated to true, print a success message and return the answer
    colour_print('Accepted.', 'green')
    return answer

# test:
# num = 50
# ask(f'Please input an integer above {num}: ', ["all(char.isdigit() for char in answer)", "int(answer) > var['num']"], {"num": num}, ['This is not a number.', 'This is not larger than 50.'])