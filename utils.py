# Utilities

import settings

def window_dimensions_percentage(dimension, percentage):
    
    if dimension == True:

        return (settings.WIDTH / 100) * percentage
    
    else:

        return (settings.HEIGHT / 100) * percentage

