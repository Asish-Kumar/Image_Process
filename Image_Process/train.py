import face_recognition
import glob
import pickle

# In this we are training the modal with many images of same person and then
# applying face_recognition on another image

# Get the directory of sample images for training
extensions = ["*.jpg", "*.png"]
file_names = []
for ext in extensions:
    for filename in glob.glob(ext):
        file_names.append(filename)

known_face_encodings = []

for image in file_names:
    person_image = face_recognition.load_image_file(image)
    person_face_encoding = face_recognition.face_encodings(person_image)[0]

    known_face_encodings.append(person_face_encoding)

with open("known_face_encoding.kfe", "wb") as pfile:
    pickle.dump(known_face_encodings, pfile)