import mediapipe as mp
import cv2


class HandDetector:
    def __init__(self):
        self.hands = mp.solutions.hands
        self.mpHands = self.hands.Hands(min_detection_confidence=0.7, max_num_hands=1)
        self.drawing = mp.solutions.drawing_utils

    def findPosition(self, img, handNo=0):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for i, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([i, cx, cy])
        return lmList

    def drawHands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.mpHands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            handLms = self.results.multi_hand_landmarks[0]
            self.drawing.draw_landmarks(img, handLms, self.hands.HAND_CONNECTIONS)
        return img
