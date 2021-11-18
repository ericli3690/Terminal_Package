"""PRINTER.PY
Printing functions, including colour_printing any string and stalling for time."""

import time

# list of accepted colours as dict
colours = {'black': 30, 'red': 31, 'green': 32, 'yellow': 33, 'blue': 34, 'purple': 35, 'cyan': 36, 'white': 37}

def colour_print(text:str, colour:str, is_input=False, insert_end='\n'):
  """colour_print(text, colour, is_input, insert_end='\n')
  Prints the text parameter as a given colour.
  Colours are stored in a static dictionary, with colour codes sourced from 'ozzmaker'
  If the provided colour to recolour the text as is a valid colour in the dictionary, then it will print that statement (and that statement only) as the given colour, else it will print an error message.
  insert_end is used for the 'end' parameter in print statements; is_input will allow an input to be created instead."""
  
  # colours.get checks if the colour provided in the parameters matches any key in the dictionary
  if colours.get(colour):
    # print <start colour><text><end colour>, end="<end>"
    if is_input:
      input(f"\033[1;{colours[colour]};40m{text}\033[1;37;40m")
    else:
      print(f"\033[1;{colours[colour]};40m{text}\033[1;37;40m", end=insert_end)
  else:
    # throw error, colour not found
    raise ValueError("Invalid Colour: " + colour)

def coloured(text:str, colour:str):
  """coloured(text, colour)
  Returns the text parameter as a given colour.
  Colours are stored in a static dictionary, with colour codes sourced from 'ozzmaker'
  If the provided colour to recolour the text as is a valid colour in the dictionary, then it will return that statement (and that statement only) as the given colour, else it will print an error message."""
  # colour located in colours dictionary
  if colours.get(colour):
    # return the text with the surrounding colour markers
    return f"\033[1;{colours[colour]};40m{text}\033[1;37;40m"
  else:
    # else raise an error, colour not found
    raise ValueError("Invalid Colour: " + colour)

def marker(colour:str='white'):
  """coloured(text, colour)
  Returns the escape sequence for a given colour.
  Colours are stored in a static dictionary, with colour codes sourced from 'ozzmaker'
  If the provided colour to recolour the text as is a valid colour in the dictionary, then it will return the escape sequence to toggle that colour on, else it will print an error message."""
  if colours.get(colour):
    return f"\033[1;{colours[colour]};40m"
  else:
    raise ValueError("Invalid Colour: " + colour)

def delay(interval):
  """delay(interval):
  Repeatedly refreshes the line, inputting a new dot every second until the amount of dots equals parameter INTERVAL (in seconds)"""
  dots_to_print = ' '
  for dot in range(interval):
    dots_to_print += '.'
    print(dots_to_print, end='\r')
    # \r clears the line
    time.sleep(1)
  print()