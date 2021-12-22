from terminal_package import ask, nest, color_print

color_print("TERMINAL PACKAGE VERSION 2.0\n", 'yellow')


###########################


color_print(nest("TESTER SCRIPT", left_right_padding=2), 'red')
print()

# testing nest
print(nest(nest("The name's Bond.\nJames Bond.", "-", "|", "o", 2, 1), '-', '|', 'o', 2, 1))

print()

# passed variable
num = 100

# my filter
def over_num(reply):
  if all(char.isdigit() for char in reply):
    if int(reply) > num:
      return True, "Accepted."
    else:
      return False, f"This is not larger than {num}."
  else:
    return False, "This is not a number."

# ask
ask(
  f"Please input an integer above {num}: ",
  over_num
  # ,True,
  # {"on_true": True, "on_false": True},
  # {"success": "yellow", "failure": "blue"}
)

######################################