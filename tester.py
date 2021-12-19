from local_tools.asker import ask

print("Testing asker.ask...\n")

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