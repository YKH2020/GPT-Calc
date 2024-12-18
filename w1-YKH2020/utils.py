# This utils module should be imported and used in main.py
# Don't change any code in this module.

def str_to_bool(val):
    """
    Convert a string to a boolean, like: yes, y, '', will be true
    otherwise will be false.
    """
    true_vals = ['yes', 'y', '']
    false_vals = ['no', 'n']
    try:
        val = val.lower()
    except AttributeError:
        val = str(val).lower()
    if val in true_vals:
        return True
    elif val in false_vals:
        return False
