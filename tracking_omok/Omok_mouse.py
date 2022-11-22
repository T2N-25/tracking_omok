import pyautogui
from tracking import hand_tracking
from tracking import eye_tracking

def get_mouse(type):
    cb = False
    if type == 'mouse':
        # mouse
        cx, cy = pyautogui.position()
        cx = round((cx - 931)/50)
        cy = round((cy - 372)/50)
    elif type == 'hand':
        # hand
        cb, cx, cy = hand_tracking.get_hand_position()
        cx = round((cx - 1200)/50)
        cy = round((cy - 500)/50)
    elif type == 'eyes':
        # eye
        cb, cx, cy = eye_tracking.get_eyes_position()
        cx = round((cx - 1200)/50)
        cy = round((cy - 500)/50)
    if cx < 0:
        cx = 0
    if cx > 14:
        cx = 14
    if cy < 0:
        cy = 0
    if cy > 14:
        cy = 14
    return cb, cx, cy