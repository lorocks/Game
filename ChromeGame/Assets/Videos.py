import cv2

BIRDVID = cv2.VideoCapture("Assets/Video/videoplayback.mp4")
CATVID = cv2.VideoCapture("Assets/cat/cat.mp4")
CACTUS_DEATH = cv2.VideoCapture("Assets/Video/CactusDeath.mp4")
BOULDER_DEATH = cv2.VideoCapture("Assets/Video/BoulderDeath.mp4")

VIDEO = [BIRDVID, CATVID, CACTUS_DEATH, BOULDER_DEATH]

def movie(num):
    while (VIDEO[num].isOpened()):
        ret, frame = VIDEO[num].read()
        if ret == True:
            cv2.imshow('Frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    VIDEO[num].release()
    cv2.destroyAllWindows()