import os
from withOpen import with_open_write, with_open_read
from folder import createFolder

# get the word saved

def wordSaved(word, data):
  if createFolder("words"):
      if not (os.path.exists('{}.text'.format(word))):
          with_open_write(word, 'text', 'w', data)
          return True
  else:
      return False