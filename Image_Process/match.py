import face_recognition
from PIL import Image, ImageDraw
import pickle
import os.path
known_faces_encodings = []

if not os.path.isfile("known_face_encoding.kfe"):
    # Do not remove this import train line, by importing it we are actually running train.py
    import train

with open("known_face_encoding.kfe", "rb") as pfile:
    known_faces_encodings = pickle.load(pfile)

# Loading unknown image
unknown_image = face_recognition.load_image_file("/home/yuri/IdeaProjects/"
                                                 "Image_Process/unknown_image/unknown_image.jpg")
# Determining all the faces in the unknown image
face_locations = face_recognition.face_locations(unknown_image)
# Generating face_encoding for each face found in unknown image
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
pil_image = Image.fromarray(unknown_image)
# Create a Pillow ImageDraw Draw instance to draw with
draw = ImageDraw.Draw(pil_image)

# Loop through each face found in the unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # Check if the face in the unknown image is a match to any of the known faces
    # 0.6 is tolerence, less is more strict
    matches = face_recognition.compare_faces(known_faces_encodings, face_encoding, 0.4)

    # If the match is found in the known_faces_encodings, draw a box around it
    if True in matches:
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

# Remove the drawing library from memory as per the pillow docs
del draw

# Display the resulting image
pil_image.show()

# You can also save a copy of the new image to disk if you want by uncommenting this line
# pil_image.save("image_with_boxes.jpg")
