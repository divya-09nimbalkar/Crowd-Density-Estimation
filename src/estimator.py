import cv2
import os

def estimate_density(image_path: str) -> str:
    """Estimate crowd density from an image using simple feature detection."""
    if not os.path.exists(image_path):
        return "❌ File not found"

    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use simple corner detection as a proxy for crowd features
    corners = cv2.goodFeaturesToTrack(gray, maxCorners=500, qualityLevel=0.01, minDistance=10)

    if corners is None:
        return "⚠️ No crowd detected"

    count = len(corners)

    # Simple heuristic: low, medium, high density
    if count < 100:
        density = "Low"
    elif count < 300:
        density = "Medium"
    else:
        density = "High"

    return f"✅ Crowd density estimated: {density} ({count} features)"
