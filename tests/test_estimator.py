import pytest
from src.estimator import estimate_density

def test_invalid_file():
    assert "File not found" in estimate_density("nonexistent.jpg")

def test_valid_image(tmp_path):
    # Placeholder: create a blank image for testing
    import cv2, numpy as np
    test_file = tmp_path / "crowd.jpg"
    blank = np.zeros((100, 100, 3), dtype=np.uint8)
    cv2.imwrite(str(test_file), blank)
    result = estimate_density(str(test_file))
    assert isinstance(result, str)
