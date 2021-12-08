import cv2


BIRDVID = cv2.VideoCapture("Assets/bird/videoplayback.mp4")
CATVID = cv2.VideoCapture("Assets/cat/cat.mp4")

def movie(num):
    if num == 1:
        while (BIRDVID.isOpened()):
            ret, frame = BIRDVID.read()
            if ret == True:
                cv2.imshow('Frame', frame)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break
        BIRDVID.release()
    if num == 2:
        while (CATVID.isOpened()):
            ret, frame = CATVID.read()
            if ret == True:
                cv2.imshow('Frame', frame)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break
        CATVID.release()
    cv2.destroyAllWindows()