class DotDict(dict):
    def __getattr__(*args):
        val = dict.get(*args)
        if type(val) is dict:
            val = DotDict(val)
        return val
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def clear_screen() -> None:
    import os
    import sys

    if sys.platform.startswith(('win32')):
        os.system('cls')
    elif sys.platform.startswith(('linux', 'cygwin', 'darwin', 'freebsd')):
        os.system('clear')


def get_file_path(filename: str) -> str:
    '''Get file path relative to utils.py'''
    import os.path

    return os.path.join(os.path.dirname(__file__), filename)
