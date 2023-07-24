#helpers funtions

# Check if an iumput is a number 
def is_not_number(value):
    try:
        float_value = float(value)
        return not isinstance(float_value, (int, float))
    except ValueError:
        return True

# Create class name
def class_name(filename):
    filename = str.replace(filename, '.csv', '')
    filename = str.replace(filename, '_', ' ')
    filename = str.replace(filename, '-', ' ')

    filename = str.title(filename)
    filename = str.replace(filename, ' ', '')
    return filename

# Handle yes 1 or no 0 answers
def yes_or_no(answer):
    while(answer != '1' and answer != '0'):
        answer = input('Enter 1 for yes 0 for no : ')
    return answer