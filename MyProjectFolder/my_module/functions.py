"""A collection of function for doing my project."""

#takes the inputs and convert the ingredient amount as needed using if loops
   
def flour_convertor(from_unit, to_unit, volume):
    '''
    Converts unit of flour to other desired unit

    Parameters
    ----------
    from_unit: string
        Unit to be converted from
    to_unit:
        Unit to be converted to
    volume:
        however much of from_unit to be converted to to_unit
    Returns
    --------
    string: states the conversion
    '''
    if from_unit == 'cups' and to_unit == 'grams':
        print (str(volume) + ' cups is equal to ' + str(volume*150) + ' grams')
        
    elif from_unit == ' grams' and to_unit == 'cups':
        print (str(volume) + 'grams is equal to ' + str(volume/150) + ' cups')
        
    elif from_unit == 'cups' and to_unit == 'ounces':
        print (str(volume) + ' cups is equal to ' + str(volume*5) + ' ounces')
        
    elif from_unit == 'ounces' and to_unit == 'cups':
        print (str(volume) + ' ounces is equal to ' + str(volume/5) + ' cups')
        
    elif from_unit == ' ounces' and to_unit == 'grams':
        print (str(volume) + ' ounces is equal to ' + str(volume*30) + ' grams')
        
    elif from_unit == 'grams' and to_unit == 'ounces':
        print (str(volume) + ' grams is equal to ' + str(volume/30) + ' ounces')
        

def cocoa_convertor(from_unit, to_unit, volume):
    '''
    Converts unit of cocoa to other desired unit

    Parameters
    ----------
    from_unit: string
        Unit to be converted from
    to_unit:
        Unit to be converted to
    volume:
        however much of from_unit to be converted to to_unit
    Returns
    --------
    string: states the conversion
    '''
    if from_unit == 'cups' and to_unit == 'grams':
        print (str(volume) + ' cups is equal to ' + str(volume*120) + ' grams')
        
    elif from_unit == ' grams' and to_unit == 'cups':
        print (str(volume) + 'grams is equal to ' + str(volume/120) + ' cups')
        
    elif from_unit == 'cups' and to_unit == 'ounces':
        print (str(volume) + ' cups is equal to ' + str(volume*4) + ' ounces')
        
    elif from_unit == 'ounces' and to_unit == 'cups':
        print (str(volume) + ' ounces is equal to ' + str(volume/4) + ' cups')
        
    elif from_unit == ' ounces' and to_unit == 'grams':
        print (str(volume) + ' ounces is equal to ' + str(volume*30) + ' grams')
        
    elif from_unit == 'grams' and to_unit == 'ounces':
        print (str(volume) + ' grams is equal to ' + str(volume/30) + ' ounces')
        

def bsugar_convertor(from_unit, to_unit, volume): 
    '''
    Converts unit of brown sugar to other desired unit

    Parameters
    ----------
    from_unit: string
        Unit to be converted from
    to_unit:
        Unit to be converted to
    volume:
        however much of from_unit to be converted to to_unit
    Returns
    --------
    string: states the conversion
    '''
    if from_unit == 'cups' and to_unit == 'grams':
        print (str(volume) + ' cups is equal to ' + str(volume*180) + ' grams')
        
    elif from_unit == ' grams' and to_unit == 'cups':
        print (str(volume) + 'grams is equal to ' + str(volume/180) + ' cups')
        
    elif from_unit == 'cups' and to_unit == 'ounces':
        print (str(volume) + ' cups is equal to ' + str(volume*6) + ' ounces')
        
    elif from_unit == 'ounces' and to_unit == 'cups':
        print (str(volume) + ' ounces is equal to ' + str(volume/6) + ' cups')
        
    elif from_unit == ' ounces' and to_unit == 'grams':
        print (str(volume) + ' ounces is equal to ' + str(volume*30) + ' grams')
        
    elif from_unit == 'grams' and to_unit == 'ounces':
        print (str(volume) + ' grams is equal to ' + str(volume/30) + ' ounces')
        

def isugar_convertor(from_unit, to_unit, volume): 
    '''
    Converts unit of icing sugar to other desired unit

    Parameters
    ----------
    from_unit: string
        Unit to be converted from
    to_unit:
        Unit to be converted to
    volume:
        however much of from_unit to be converted to to_unit
    Returns
    --------
    string: states the conversion
    '''
    if from_unit == 'cups' and to_unit == 'grams':
        print (str(volume) + ' cups is equal to ' + str(volume*120) + ' grams')
        
    elif from_unit == ' grams' and to_unit == 'cups':
        print (str(volume) + 'grams is equal to ' + str(volume/120) + ' cups')
        
    elif from_unit == 'cups' and to_unit == 'ounces':
        print (str(volume) + ' cups is equal to ' + str(volume*4) + ' ounces')
        
    elif from_unit == 'ounces' and to_unit == 'cups':
        print (str(volume) + ' ounces is equal to ' + str(volume/4) + ' cups')
        
    elif from_unit == ' ounces' and to_unit == 'grams':
        print (str(volume) + ' ounces is equal to ' + str(volume*30) + ' grams')
        
    elif from_unit == 'grams' and to_unit == 'ounces':
        print (str(volume) + ' grams is equal to ' + str(volume/30) + ' ounces')
        

def sugar_convertor(from_unit, to_unit, volume):  
    '''
    Converts unit of sugar to other desired unit

    Parameters
    ----------
    from_unit: string
        Unit to be converted from
    to_unit:
        Unit to be converted to
    volume:
        however much of from_unit to be converted to to_unit
    Returns
    --------
    string: states the conversion
    '''
    if from_unit == 'cups' and to_unit == 'grams':
        print (str(volume) + ' cups is equal to ' + str(volume*240) + ' grams')
        
    elif from_unit == ' grams' and to_unit == 'cups':
        print (str(volume) + 'grams is equal to ' + str(volume/240) + ' cups')
        
    elif from_unit == 'cups' and to_unit == 'ounces':
        print (str(volume) + ' cups is equal to ' + str(volume*8) + ' ounces')
        
    elif from_unit == 'ounces' and to_unit == 'cups':
        print (str(volume) + ' ounces is equal to ' + str(volume/8) + ' cups')
        
    elif from_unit == ' ounces' and to_unit == 'grams':
        print (str(volume) + ' ounces is equal to ' + str(volume*30) + ' grams')
        
    elif from_unit == 'grams' and to_unit == 'ounces':
        print (str(volume) + ' grams is equal to ' + str(volume/30) + ' ounces')

        
def butter_convertor(from_unit, to_unit, volume): 
    '''
    Converts unit of butter to other desired unit

    Parameters
    ----------
    from_unit: string
        Unit to be converted from
    to_unit:
        Unit to be converted to
    volume:
        however much of from_unit to be converted to to_unit
    Returns
    --------
    string: states the conversion
    '''
    if from_unit == 'cups' and to_unit == 'grams':
        print (str(volume) + ' cups is equal to ' + str(volume*225) + ' grams')
        
    elif from_unit == ' grams' and to_unit == 'cups':
        print (str(volume) + 'grams is equal to ' + str(volume/225) + ' cups')
        
    elif from_unit == 'cups' and to_unit == 'ounces':
        print (str(volume) + ' cups is equal to ' + str(volume*8) + ' ounces')
        
    elif from_unit == 'ounces' and to_unit == 'cups':
        print (str(volume) + ' ounces is equal to ' + str(volume/8) + ' cups')
        
    elif from_unit == ' ounces' and to_unit == 'grams':
        print (str(volume) + ' ounces is equal to ' + str(volume*28.125) + ' grams')
        
    elif from_unit == 'grams' and to_unit == 'ounces':
        print (str(volume) + ' grams is equal to ' + str(volume/28.125) + ' ounces')

        
def check_convertor(ingredient, from_unit, to_unit, volume):
    '''
    checks input ingredient and runs the corresponding convertor

    Parameters
    ----------
    ingredient: string
        Ingredient to convert
    from_unit: string
        Unit to be converted from
    to_unit:
        Unit to be converted to
    volume:
        however much of from_unit to be converted to to_unit
    Returns
    --------
    Runs the corresponding convertor to print a string stating conversion
    '''
    if ingredient == 'flour':
        flour_convertor(from_unit, to_unit, volume)
        
    elif ingredient == 'cocoa':
        cocoa_convertor(from_unit, to_unit, volume)
        
    elif ingredient == 'brown sugar':
        bsugar_convertor(from_unit, to_unit, volume)
        
    elif ingredient == 'icing sugar':
        isugar_convertor(from_unit, to_unit, volume)
        
    elif ingredient == 'sugar':
        sugar_convertor(from_unit, to_unit, volume)
        
    elif ingredient == 'butter':
        butter_convertor(from_unit, to_unit, volume)
        

class PortionChange():
    '''
    This class converts to desired serving amount
    
    input: integer
    output: integer
    '''
    def __init__(self, initial_servings, desired_servings):
        self.initial_servings = initial_servings
        self.desired_servings = desired_servings
        
    def change_portions(self, output):
        making_amount = output/self.initial_servings*self.desired_servings
        print ('Actual amount: ' + str(making_amount))
        
        
