from local_tools.printer import colour_print
from local_tools.validate import ask

colour_print("LOCAL TOOLS VERSION 3.1\n", 'yellow')

# test of validate:
print("Testing validate.ask...\n")

# passed variable
num = 100

ask(

  # prompt
  f"Please input an integer above {num}: ",

  # conditions
  [
    "all(char.isdigit() for char in answer)",
    "int(answer) > var['num']"
  ],

  # corresponding errors
  [
    "This is not a number.",
    "This is not larger than 50."
  ],

  # clear console
  False,

  # passed variables
  {
    "num": num
  },

  # catch null
  True

)