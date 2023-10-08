import cv2
import numpy as np

# Load the normal image
normal_image = cv2.imread(r"D:\Dinesh-Kumar\Downloads\STUDENT_P.JPG")

# Convert the image to grayscale
gray_image = cv2.cvtColor(normal_image, cv2.COLOR_BGR2GRAY)

# Apply a pseudo-color mapping for NIR effect
# You can experiment with different color maps for desired results
#nir_image = cv2.applyColorMap(gray_image, cv2.COLORMAP_JET)

nir_image2 = cv2.applyColorMap(gray_image, cv2.COLORMAP_BONE)


# Concatenate the original and NIR images side by side
comparison_image = np.hstack((normal_image, nir_image2))

# Save the comparison image
cv2.imwrite('comparison_image.jpg', comparison_image)

# Display the comparison image
cv2.imshow('Comparison Image', comparison_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
