"""VALIDATE.PY
Validates user input and handles errors
Includes:
- log_error(reason): print an error statement to the console with the provided reason.
- validate(to_check, required_type): check if the parameter to_check is of the same type as required_type, returning to_check if they are identical or False if they are not
  - Additionally, if required_type is 'yyyymmdd', it will return to_check as a datetime object if successful
- ask_question_validate(prompt, type_of_answer): repeatedly asks the user for an input of parameter prompt until it gets one matching type_of_answer; it does this checking through validate()
- ask_question_eval_vague(prompt, conditions): like the above but does not rely on validate, instead allowing the programmer to input the code to run when it is called, evaling it
- ask_question_eval_explicit(prompt, conditions): like the above but uses a list of conditions, allowing it to log exactly which condition was unfulfilled instead of a general error message
- ask_question_eval_explicit_friendly(prompt, conditions, errors): like the above but adds a list of errors, allowing it to long which condition was unfulfilled in a human manner
"""

# imports
# colour_printer for colour printing strings, calendar and datetime for validating dates, timezone to make those dates mdt; create mdt constant
from colour_printer import colour_print
import calendar
import datetime
from pytz import timezone
CALGARY_TIMEZONE = timezone('America/Edmonton')

def log_error(reason="Please re-input."):
    """log_error(reason)
    Prints an error message in red, including reason"""
    colour_print("Denied. This is not a valid value: " + reason, 'red')

def validate(to_check, required_type):
  """validate(to_check, required_type)
  Checks if to_check matches multiple types, returning to_check if it does and False if it doesn't
  If the type to check is yyyymmdd, it will return to_check as a datetime object on success
  Otherwise, it prints an error to the console using log_error
  These types include:
  - int: all characters in the string are a number
  - yn: either the character y or n
  - str: the type of to_check is a string
  - yyyymmdd: checks that:
    - it is eight long
    - it is an int
    - month is valid
    - day is valid, based on month"""
  if required_type == 'int' and all(char.isdigit() for char in to_check):
    # if every character isdigit
    return to_check
  elif required_type == 'yn' and (to_check == 'y' or to_check == 'n'):
    # if either the character y or n
    return to_check
  elif required_type == 'str' and type(to_check) == str:
    # if its just a string
    return to_check
  elif required_type == 'yyyymmdd':
    # if it is a date, ex. one to count down to
    # heavily nested to avoid using calendar.monthrange on an invalid parameter, which would throw an error and stop the program
    # defines year, month, and day, to be extracted from the eight-character string
    year, month, day = 0000, 00, 00
    # if the length of the eight-character string is indeed eight and it is an int
    if len(to_check) == 8 and all(char.isdigit() for char in to_check):
      # break it up into year, month, and date
      year = int(to_check[0:4])
      month = int(to_check[4:6])
      day = int(to_check[6:8])
      # if month is 1:13
      if month <= 12 and month > 0 and year > 0:
        # use monthrange to find the amount of days in month
        days_in_month = calendar.monthrange(year, month)[1]
        # if the day is equal to or less than the days in this month (also above 0)
        if day <= days_in_month and day > 0:
          # return as an aware datetime object, ie. has knowledge of timezones
          return datetime.datetime(
            int(year),
            int(month),
            int(day),
            0, 0, 0, 0,
            CALGARY_TIMEZONE)
        else:
          log_error('Date is out of range.')
          return False
      else:
        log_error('Month or year is out of range.')
        return False
    else:
      log_error('Incorrect format.')
      return False
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

# ask_question_eval_explicit_friendly('int50+ ', ['all(char.isdigit() for char in answer)', 'int(answer) > 50'], ['This is not a number.', 'This is not larger than 50.'])