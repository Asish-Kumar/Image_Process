import cv2
import face_recognition
import os


def just_pass():
    pass


capture_video = cv2.VideoCapture(os.getcwd()+"/Video_mp4/video.mp4")
image_found, image = capture_video.read()
cv2.imwrite("temp_image.jpg", image)
img_count = 0
count = 1
upto = 30
second = 1
max_face_image = image
max_face_loc = face_recognition.face_locations(face_recognition.load_image_file("temp_image.jpg"))
max_num_faces = 0

c1 = c2 = image

switcher = {
    1: c1,
    2: c2
}

a = [0, 0]

while image_found:
    if second <= 2:
        if count <= upto:
            image_file = face_recognition.load_image_file("temp_image.jpg")
            face_loc = face_recognition.face_locations(image_file)  # returns a list of tuple of face location
            num_faces = len(face_loc)  # total number of faces found in image

            if num_faces > max_num_faces:
                max_num_faces = num_faces
                max_face_loc = face_loc
                max_face_image = image
    # cv2.imwrite(os.getcwd()+"/frames/frame%d.jpg" % count, image)     # save frame as JPEG file
            image_found, image = capture_video.read()
            image_found, image = capture_video.read()

            cv2.imwrite("temp_image.jpg", image)
            print('Read a new frame: %d '%count, image_found)
            count += 2
        else:
            upto += 30
            switcher[second] = max_face_image
            a[second-1] = max_num_faces
            second += 1

            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

    else:
        second = 1
        maximum = a.index(max(a))
        maximum_face_image = switcher[maximum+1]
        cv2.imwrite(os.getcwd()+"/frames/frame%d.jpg" % img_count, maximum_face_image)
        img_count += 1
        max_num_faces = 0
import match
match.just_pass()
