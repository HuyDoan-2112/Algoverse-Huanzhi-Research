import cv2 
import numpy as np
from typing import Optional

def blur_image(img, ksize: int = 15) -> np.ndarray:
    """Applies Gaussian blur to the image."""
    return cv2.GaussianBlur(img, (ksize, ksize), 0)

def grayscale_image(img) -> np.ndarray:
    """Converts the image to grayscale."""
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def edge_detection(img, low_threshold: int = 100, high_threshold: int = 200) -> np.ndarray:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.Canny(gray, low_threshold, high_threshold)

def brighten_image(img, alpha: float = 1.5, beta: int = 30) -> np.ndarray:
    return cv2.convertScaleAbs(img, alpha=alpha, beta=beta)