#helpers funtions

# Check if an iumput is a number 
def is_not_number(value):
    try:
        float_value = float(value)
        return not isinstance(float_value, (int, float))
    except ValueError:
        return True