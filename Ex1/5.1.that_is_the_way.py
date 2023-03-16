import re
import os


def get_files(path):
    """
    Find all files in a specific directory which are start in 'deep'
    :param path: Path to directory
    :return: List of All files in the directory which are start in 'deep'
    """
    files = os.listdir(path)
    return [name for name in files if re.match('^deep', name)]
