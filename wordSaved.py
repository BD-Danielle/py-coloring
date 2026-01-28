import os

# get the word saved


def word_saved(word):
    cwd = os.getcwd()
    dir = os.path.join(cwd, "words")
    os.chdir(dir)
    if not (os.path.exists('{}.json'.format(word))):
        print('word unexistent')
        return False
    else:
        print('word existed')
        return True
