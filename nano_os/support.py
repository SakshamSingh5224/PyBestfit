import random

""" List of some MIPS registers available for programs usage """
REGISTERS = ['r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15']

""" List of basic process states, for single-task systems """
P_STATES = ['waiting', 'running', 'done']

""" Flag for testing mode, controls behavior (optional) """
TESTING = False

""" List of predefined process sizes for testing (optional) """
SIZES = [10, 20, 30, 40]

""" List to store errors encountered during execution (optional) """
ERRORS = []


def g_int_value(a=None, b=None):
  """
  Generates a random integer value within a range or a single random value.

  Args:
      a (int, optional): Lower bound for the random range. Defaults to None.
      b (int, optional): Upper bound for the random range. Defaults to None.

  Returns:
      int: A random integer value.
  """

  if a is None and b is None:
    return random.randint(1, 100)  # Random value between 1 and 100 (inclusive)
  elif isinstance(a, int) and isinstance(b, int) and a <= b:
    return random.randint(a, b)  # Random value within the specified range
  else:
    raise ValueError("Invalid arguments for g_int_value: a and b must be integers, and a <= b")


def g_list_value(lst):
  """
  Selects a random element from a list.

  Args:
      lst (list): The list to choose an element from.

  Returns:
      any: A random element from the list.

  Raises:
      TypeError: If the argument is not a list.
  """

  if isinstance(lst, list):
    random.shuffle(lst)  # Shuffle the list for randomness
    return lst[random.randint(0, len(lst)-1)]  # Return a random element
  else:
    raise TypeError("g_list_value requires a list argument")
