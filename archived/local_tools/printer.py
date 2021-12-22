"""
PRINTER.PY VERSION 2.1
Printing functions, including color_printing any string.
"""

# list of accepted colors as dict
colors = {'black': 30, 'red': 31, 'green': 32, 'yellow': 33, 'blue': 34, 'purple': 35, 'cyan': 36, 'white': 37}

def color_print(text:str, color:str, is_input=False, insert_end='\n'):
  """color_print(text, color, is_input, insert_end='\n')
  Prints the text parameter as a given color.
  colors are stored in a static dictionary, with color codes sourced from 'ozzmaker'
  If the provided color to recolor the text as is a valid color in the dictionary, then it will print that statement (and that statement only) as the given color, else it will print an error message.
  insert_end is used for the 'end' parameter in print statements; is_input will allow an input to be created instead."""
  
  # colors.get checks if the color provided in the parameters matches any key in the dictionary
  if colors.get(color):
    # print <start color><text><end color>, end="<end>"
    if is_input:
      input(f"\033[1;{colors[color]};40m{text}\033[1;37;40m")
    else:
      print(f"\033[1;{colors[color]};40m{text}\033[1;37;40m", end=insert_end)
  else:
    # throw error, color not found
    raise ValueError("Invalid color: " + color)

def colored(text:str, color:str):
  """colored(text, color)
  Returns the text parameter as a given color.
  colors are stored in a static dictionary, with color codes sourced from 'ozzmaker'
  If the provided color to recolor the text as is a valid color in the dictionary, then it will return that statement (and that statement only) as the given color, else it will print an error message."""
  # color located in colors dictionary
  if colors.get(color):
    # return the text with the surrounding color markers
    return f"\033[1;{colors[color]};40m{text}\033[1;37;40m"
  else:
    # else raise an error, color not found
    raise ValueError("Invalid color: " + color)

def marker(color:str='white'):
  """colored(text, color)
  Returns the escape sequence for a given color.
  colors are stored in a static dictionary, with color codes sourced from 'ozzmaker'
  If the provided color to recolor the text as is a valid color in the dictionary, then it will return the escape sequence to toggle that color on, else it will print an error message."""
  if colors.get(color):
    return f"\033[1;{colors[color]};40m"
  else:
    raise ValueError("Invalid color: " + color)