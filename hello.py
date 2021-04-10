#!/usr/bin/python3 -tt
""" #!/usr/bin/python -tt """
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""A tiny Python program to check that Python is working.
Try running this program from the command line like this:
  python hello.py
  python hello.py Alice
That should print:
  Hello World -or- Hello Alice
Try changing the 'Hello' to 'Howdy' and run again.
Once you have that working, you're ready for class -- you can edit
and run Python code; now you just need to learn Python!
"""

import sys


def repeat(s, explaim):
    """
     returns string s 3 times
    """
    result = s + s + s # can also use s*3 which is faster (why?)
    if explaim:
        result = result + '!!!'
    return result

# Define a main() function that prints a little greeting.
def main():
  # Get the name from the command line, using 'World' as a fallback.
  print (sys.argv)
  if len(sys.argv) >= 2:
      name = sys.argv[1]
  else:
      name = 'World'
  print ('Hello  ', name)
  if len(sys.argv) > 2:
      str = repeat(sys.argv[2], True)
      print (str)
  else:
      print ('less than 2 arguments')
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
