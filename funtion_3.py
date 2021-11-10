import cv2
import os, glob
import os.path
import face_recognition
from PIL import Image

def face(imgMinju,imgTest):
    imgMinju = cv2.cvtColor(imgMinju, cv2.COLOR_BGR2RGB)  # 사진 그리기
    imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)  # 사진 그리기
    # 분홍색 박스 그리기
    faceLoc = face_recognition.face_locations(imgMinju)[0]
    encodeElon = face_recognition.face_encodings(imgMinju)[0]  # 사진에서 얼굴 찾기
    cv2.rectangle(imgMinju, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)  # 박스 그리기

    faceLocTest = face_recognition.face_locations(imgTest)[0]  # 얼굴 검출
    encodeTest = face_recognition.face_encodings(imgTest)[0]
    cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)
    # ↑분홍색 박스 그리는 부분 #
    results = face_recognition.compare_faces([encodeElon], encodeTest)  # 동일 인물검증
    faceDis = face_recognition.face_distance([encodeElon], encodeTest)  # 얼마나 다른가를 검출 => 숫자가 낮을수록 좋다.

    cv2.putText(imgTest, f'{results} {round(faceDis[0], 2)}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255),
                2)  # faceDis 값을 imgTest파일에 그린다.
    difference = faceDis * 100
    print(results)
    print(difference, "%")

    #cv2.imshow('my_image', imgMinju)
    #cv2.imshow('minju', imgTest)
    #cv2.waitKey(0)
def file_count(file_location,first):
    Filename = os.listdir(file_location)
    #print(Filename)
    #print(len(Filename))
    #now = first+Filename[0]
    #print("'"+now+"'")

    #print(file_numbers)
    #print(Filename[y])

    first = 'ImagesBasic/'
    file_numbers = int(len(Filename))
    y = int(file_numbers - 2)
    file = first+Filename[y]
    #print(file)
    image = Image.open(file)
    image.show()
def count(file_location,basic_location):
    first_1 = basic_location  # 'ImagesBasic/'
    file_list=file_location + basic_location #r''+'ImagesBasic/'
    Filename = os.listdir(file_list)
    for i in Filename:
        file= first_1
        print(1)
        file_list = file_location + basic_location  # r''+'ImagesBasic/'
        print(2)
        #print(i)
        print(file)
        imgTest = face_recognition.load_image_file(file)#권한에러
        print(3)
        imgMinju = face_recognition.load_image_file('ImagesBasic/minju.jpg')
        print(4)
        face(imgMinju, imgTest)
        file = first_1 + i




    #imgTest = face_recognition.load_image_file(file)
    #imgMinju = face_recognition.load_image_file('ImagesBasic/minju.jpg')
    #face(imgMinju, imgTest)

    #file_numbers = int(len(Filename))
    #y = int(file_numbers - 2)
    #file = first_1+Filename[y]
    #print(file)
    #imgTest = face_recognition.load_image_file(file)
    #imgMinju = face_recognition.load_image_file('ImagesBasic/minju.jpg')
    #print(file)
    #face(imgMinju,imgTest)


#imgMinju = face_recognition.load_image_file(file)  # 파라미터에 카메라에서 찍은 사진경로입력

# 파라미터에 카메라에서 찍은 사진경로입력
#face(imgMinju,imgTest)

file_location = r''
basic_location = 'ImagesBasic/'
count(file_location,basic_location)

