import pyautogui

def handle_action(action):
    if action == "play":
        pyautogui.press('space')
    elif action == "pause":
        pyautogui.press('space')
    elif action == "forward":
        pyautogui.press('right')
    elif action == "backward":
        pyautogui.press('left')
    elif action == "next":
        pyautogui.hotkey('ctrl', 'right')
    elif action == "previous":
        pyautogui.hotkey('ctrl', 'left')
    elif action == "volume_up":
        pyautogui.press('volumeup')
    elif action == "volume_down":
        pyautogui.press('volumedown')