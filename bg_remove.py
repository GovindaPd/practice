import cv2, cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

vid = cv2.VideoCapture(0)
vid.set(3,640)
vid.set(4,480)

bg_img = cv2.imread("c.jpg")
seg = SelfiSegmentation()
while True:
    _,video = vid.read()
    vid_rmbg = seg.removeBG(video, bg_img, threshold=0.2)
    cv2.imshow("Video", vid_rmbg)
    if cv2.waitKey(1) == ord("x"):
        break;



    
