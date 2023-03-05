import re
import os


def get_files(path):
    files = os.listdir(path)
    return [name for name in files if re.match('^deep', name)]
