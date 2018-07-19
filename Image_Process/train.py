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
person_face_encoding = []
i = 1

for image in file_names:
    person_image = face_recognition.load_image_file(image)
    person_face_location = face_recognition.face_locations(person_image)
    print("Hello", i)
    i += 1
    try:
        person_face_encoding = face_recognition.face_encodings(person_image, person_face_location)[0]
    except Exception:
        print("FACE NHI MILA")
        continue

    known_face_encodings.append(person_face_encoding)

# If known_face_encodings is empty, i.e., no face detected in the training images
if not known_face_encodings:
    print("There is no face found in any of the test images, please provide valid test images.")
else:
    with open("known_face_encoding.kfe", "wb") as pfile:
        pickle.dump(known_face_encodings, pfile)
