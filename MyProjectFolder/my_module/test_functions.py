"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import flour_convertor, cocoa_convertor, bsugar_convertor, isugar_convertor, sugar_convertor, butter_convertor, check_convertor, PortionChange
'''
These test functions should return nothing if the code runs properly as my project functions print instead of return. 
'''

def test_check_convertor():
    assert check_convertor('flour', 'grams', 'ounces', 300) == None
    
def test_PortionChange():
    x = PortionChange(5,3)
    assert x.change_portions(500) == None
