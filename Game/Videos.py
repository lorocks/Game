import cv2
import imutils
import pygame

def rescale_frame(frame, scale):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

def movie(num, Age19):
    if Age19 == False and num == 7:
        num += 1

    if num == 0:
        VIDEO = cv2.VideoCapture("Assets/Video/CactusDeath.mp4")
    elif num == 1:
        VIDEO = cv2.VideoCapture("Assets/Video/BoulderDeath.mp4")
    elif num == 2:
        VIDEO = cv2.VideoCapture("Assets/Video/ManEater.mp4")
    elif num == 3:
        VIDEO = cv2.VideoCapture("Assets/Video/Fire.mp4")
    elif num == 4:
        VIDEO = cv2.VideoCapture("Assets/Video/Lycoris.mkv")
    elif num == 5:
        VIDEO = cv2.VideoCapture("Assets/Video/Spikes.mp4")
    elif num == 6:
        VIDEO = cv2.VideoCapture("Assets/Video/Sword.mkv")
    elif num == 7:
        VIDEO = cv2.VideoCapture("Assets/Video/Drone.mp4")
    elif num == 8:
        VIDEO = cv2.VideoCapture("Assets/Video/DroneTom.mp4")
    elif num == 9:
        VIDEO = cv2.VideoCapture("Assets/Video/Rhitta.mkv")
    elif num == 10:
        VIDEO = cv2.VideoCapture("Assets/Video/Start.mp4")
    elif num == 11:
        VIDEO = cv2.VideoCapture("Assets/Video/GalandKills.mp4")
    elif num == 12:
        VIDEO = cv2.VideoCapture("Assets/Video/KillGaland.mp4")
    elif num == 13:
        VIDEO = cv2.VideoCapture("Assets/Video/OrcArmy.mp4")
    elif num == 14:
        VIDEO = cv2.VideoCapture("Assets/Video/EyeComes.mp4")
    elif num == 15:
        VIDEO = cv2.VideoCapture("Assets/Video/Eyegone.mp4")
    elif num == 16:
        VIDEO = cv2.VideoCapture("Assets/Video/Confrontation.mp4")
    elif num == 17:
        VIDEO = cv2.VideoCapture("Assets/Video/FirstHit.mkv")
    elif num == 18:
        VIDEO = cv2.VideoCapture("Assets/Video/SecondHit.mp4")
    elif num == 19:
        VIDEO = cv2.VideoCapture("Assets/Video/FinalHit.mp4")
    elif num == 20:
        VIDEO = cv2.VideoCapture("Assets/Video/GetHit1.mkv")
    elif num == 21:
        VIDEO = cv2.VideoCapture("Assets/Video/GetHit2.mkv")
    elif num == 22:
        VIDEO = cv2.VideoCapture("Assets/Video/GetHit3.mkv")

    #pygame.mixer.music.play()
    if num == -1:
        while (VIDEO.isOpened()):
            isTrue, frame = VIDEO.read()
            if not frame is None:
                frame_resized = rescale_frame(frame, scale=0.5)
            if isTrue:
                cv2.imshow("Video Resized", frame_resized)
                if cv2.waitKey(8) & 0xFF == ord("q"):
                    break
            else:
                break
    elif num == 0 or num == 1:
        while (VIDEO.isOpened()):
            isTrue, frame = VIDEO.read()
            if not frame is None:
                frame_resized = rescale_frame(frame, scale=1.75)
            if isTrue:
                cv2.imshow("Video Resized", frame_resized)
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    break
            else:
                break
    elif num == 2 or num == 8:
        while (VIDEO.isOpened()):
            isTrue, frame = VIDEO.read()
            if not frame is None:
                frame_resized = rescale_frame(frame, scale=1.5)
            if isTrue:
                cv2.imshow("Video Resized", frame_resized)
                if cv2.waitKey(35) & 0xFF == ord("q"):
                    break
            else:
                break
    elif num == 3 or num == 5:
        while (VIDEO.isOpened()):
            isTrue, frame = VIDEO.read()
            if not frame is None:
                frame_resized = rescale_frame(frame, scale=0.75)
            if isTrue:
                cv2.imshow("Video Resized", frame_resized)
                if cv2.waitKey(25) & 0xFF == ord("q"):
                    break
            else:
                break
    else:
        while (VIDEO.isOpened()):
            isTrue, frame = VIDEO.read()
            if isTrue:
                cv2.imshow('Frame', frame)
                if cv2.waitKey(25) & 0xFF == ord('q'):
                    break
            else:
                break
    VIDEO.release()
    cv2.destroyAllWindows()