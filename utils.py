# Utilities

import settings

def window_dimensions_percentage(dimension, percentage):

    """
    @param dimension: True for Width, False for Heigth
    @param percentage: Percentage of the dimension value
    """
    
    if dimension == True:

        return (settings.WIDTH / 100) * percentage
    
    else:

        return (settings.HEIGHT / 100) * percentage

