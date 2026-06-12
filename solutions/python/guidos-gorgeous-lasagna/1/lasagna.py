""" The constants are defined as follows """
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2  # Good practice to keep constants UPPERCASE

def bake_time_remaining(elapsed_bake_time):
    """ This function calculates the bake time remaining """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """ This function calculates the preparation time in minutes """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """ This function calculates the total required for baking """
    # 1. Compute prep time using your second function dynamically
    prep_time = preparation_time_in_minutes(number_of_layers)
    
    # 2. Add prep time to the actual time spent baking, then return it
    return prep_time + elapsed_bake_time

    
