import cv2
import imagezmq
from time import gmtime, strftime


image_hub = imagezmq.ImageHub()


while True:

  rpi_name, image = image_hub.recv_image()
  
  image2= cv2.resize(image, dsize=(640, 480), interpolation=cv2.INTER_AREA)  
  cv2.rectangle(image2,(160,35),(480,445),(0,255,0),3)
  cv2.imshow(rpi_name, image2)
  
  imgfile='C:/Users/Hyeok/pic/'+strftime("%Y%m%d_%H_%M_%S", gmtime())+'.png'
  cv2.imwrite(imgfile, image2)
  
  
  if cv2.waitKey(1) == ord('q'):
     break
  
  image_hub.send_reply(b'OK')
  
  
