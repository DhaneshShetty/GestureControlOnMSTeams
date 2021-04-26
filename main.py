import handmodule as htm
import cv2
import pyautogui

video = cv2.VideoCapture(0)
detector = htm.HandDetector()
mute = False

while True:
    success, img = video.read()
    image = detector.drawHands(img)
    positions = detector.findPosition(img)
    if len(positions) > 0:
        if abs(positions[8][1] - positions[4][1]) < 20 and abs(positions[8][2] - positions[4][2]) < 20 and mute:
            print("Mute")
            pyautogui.hotkey('ctrl', 'shift', 'm')
            mute = False
        if positions[10][2] < positions[12][2] and positions[6][2] < positions[8][2] and positions[14][2] < \
                positions[16][2] and positions[18][2] < positions[20][2] and not mute:
            print("Unmute")
            pyautogui.hotkey('ctrl', 'shift', 'm')
            mute = True
    cv2.imshow("Video", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
