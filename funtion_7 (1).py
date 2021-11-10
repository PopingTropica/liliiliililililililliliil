import cv2
import os, glob
import os.path
import face_recognition

import socket
import time
from imutils.video import VideoStream

#카메라 인식
import imagezmq
from time import gmtime, strftime





def file_check(file_name): #file_name 카메라에서 찍은 사진이 저장되는 위치 + 파일이름
    file_name_visit = file_name#에러방지
    if os.path.isfile(file_name_visit) == True:#file_name_visit파일이 있을경우
        return;
    else:
        file_check(file_name)

# def capture(save_file): #파일 저장 위치
#     if os.path.exists(save_file):
#         img = cv2.imread(save_file, cv2.IMREAD_COLOR)
#         cv2.imwrite(save_file, img)
#     else:
#         return;



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
    if results[0] == True:
        print("등록된 사용자입니다.")
        return;

def count(file_location,basic_location,Visiter_location):
    first_1 = basic_location  # 'ImagesBasic/'
    file_list=file_location+basic_location #r''+'ImagesBasic/'
    Filename = os.listdir(file_list)
    file_numbers = int(len(Filename))

    for i in range(file_numbers):
        x = file_numbers
        if i < x:
            file = first_1 + Filename[x - i - 1]  # r''+'ImagesBasic/'
            imgTest = face_recognition.load_image_file(file)
            print(file)
            print(Visiter_location)
            imgMinju = face_recognition.load_image_file(Visiter_location)
            face(imgMinju, imgTest)
        if i - x < 0:
            print("종료")
            return;
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

# def test_camera():
#     import cv2
#
#     capture = cv2.VideoCapture(0)  # 출력할 카메라 선택
#     capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 카메라 속성값
#     capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # 카메라 속성값
#
#     run = int(input("실행하기 위해서 1을 눌러주세요"))
#     if (run == 1):
#         while cv2.waitKey(33) < 0:
#             ret, frame = capture.read()
#             cv2.imshow("VideoFrame", frame)


image_hub = imagezmq.ImageHub()


#Visiter_location = 'ImageBasic/my_image.jpg' #카메라에서 찍은 사진이 저장되는 파일위치+파일이름
#count(file_location,basic_location,Visiter_location)
#file_location2 = 'C:/Users/Hyeok/pic/' # 파일 저장 위치 + 파일이름

rpi_name, image = image_hub.recv_image()
image2 = cv2.resize(image, dsize=(640, 480), interpolation=cv2.INTER_AREA)
cv2.rectangle(image2, (80, 32), (250, 210), (0, 255, 0), 3)
# cv2.imshow(rpi_name, image2)

imgfile = r'pic/' + 'minju' + '.png'
cv2.imwrite(r''+imgfile, image2)
image_hub.send_reply(b'OK')



while True:
    # 파일 저장

    file_location = r''
    basic_location = 'ImagesBasic/'
    Visiter_location = ''+imgfile  # 카메라에서 찍은 사진이 저장되는 파일위치+파일이름
    file_check(Visiter_location) #해당 폴더에 파일이 있는가
    print(imgfile)
    print(Visiter_location)
    count(file_location, basic_location, Visiter_location)
    os.remove(Visiter_location)#파일 삭제




