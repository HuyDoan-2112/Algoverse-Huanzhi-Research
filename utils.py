from cv_functions import *

FUNCTIONS = {
    "blur_image": blur_image,
    "grayscale_image": grayscale_image,
    "edge_detection": edge_detection,
    "brighten_image": brighten_image,

}

def get_function(prompt: str):
    for key, func in FUNCTIONS.items():
        if key in prompt.lower():
            return func
    return None

