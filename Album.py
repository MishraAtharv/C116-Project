import os
import cv2

# Set path for the Images folder
path = "C:/Users/infos/Desktop/C117 Project/Images"

# Create a list variable named Images = [ ]
images = []

# Use the for loop to check each file in the folder using os.listdir(path)
for file in os.listdir(path):
    # For each file name, use os.path.splitext(file) to separate the name and extension from a file name
    name, extension = os.path.splitext(file)
    
    # Create an if condition to check if the extension of the file matches the image extension
    if extension.lower() in ['.jpg', '.jpeg', '.png', '.gif']:
        # Create a variable file_name by concatenating the path, "/" and filename (Including both name and extension)
        file_name = os.path.join(path, file)
        
        # Use print(file_name) to make sure filenames are formed correctly
        print(file_name)
        
        # Add each file in the images list using .append()
        images.append(file_name)

# Create a variable count to store len(images)
count = len(images)

# Create a variable named frame to read the first image from the images list
frame = cv2.imread(images[0])

# Use frame.shape to capture width, height & Channels
width, height, channels = frame.shape

# Create a tuple variable size using width, height
size = (width, height)

# Use print(size) to check the result
print(size)

# Create a variable out
out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

# Create a for loop to add images to a video writer
for i in range(0, count-1):
    # Use cv2.imread() to reach each image
    img = cv2.imread(images[i])
    
    # Add the image in the video using out.write()
    out.write(img)

# Print a message to know the video is complete
print("Done")

# Release the VideoWriter
out.release()