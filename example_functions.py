# All functions taken from "Python Numerical Methods", Kong, Siauw and Bayen 
# https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html

def my_adder(a: int | float, b: int | float, c: int | float) -> int | float:
    """This function adds the inputs together

    Args:
        a (int | float): any number
        b (int | float): any number
        c (int | float): any number

    Returns:
        float | int: sum of the inputs a, b and c
    """
    
    # this is the summation
    out = a + b + c
    
    return out


def my_thermo_stat(temp: int | float, desired_temp: int | float) -> str: 
    """This function returns the status from three options based on the current and desired temperature 

    Args:
        temp (int or float): the current temperature
        desired_temp (int or float): the desired temperature

    Returns:
        str: status of any change required or not
    """
    if temp < desired_temp - 5:
        status = 'Heat'
    elif temp > desired_temp + 5:
        status = 'AC'
    else:
        status = 'off'
    return status
    
 
def have_digits(s: str) -> int:
    """This function checks if there is a digit in the string
    
    Outputs 1 as long as there is any digit in the string

    Args:
        s (str): a string with or without digits

    Returns:
        int: 1 or 0
    """
    
    out = 0
    
    # loop through the string
    for c in s:
        # check if the character is a digit
        if c.isdigit():
            out = 1
            break
            
    return out
    
def area_of_rectangle(width: int | float,height: int | float) -> int | float:
    """This function returns the area of a rectangle with a width and height

    Args:
        width (int | float): width of the rectangle
        height (int | float): height of the rectangle

    Returns:
        int | float: area of the rectangle
    """
    area = width*height
    return area


def perimeter_of_rectangle(width: int | float,height: int | float) -> int | float:
    """This function returns the perimeter of a rectangle with a width and height

    Args:
        width (int | float): width of the rectangle
        height (int | float): height of the rectangle
        
    Returns:
        int | float: perimeter of the rectangle
    """
    perimeter = 2*(width+height)
    return perimeter
